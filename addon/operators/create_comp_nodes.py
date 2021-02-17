import bpy
from addon.utility.settings import Settings


class CreateCompNodes:
    bl_name = 'olv.create_comp_nodes'
    bl_label = 'Create comp nodes for rendering'

    operator = bpy.ops

    nodes = {'Nodes': ['CompositorNodeRLayers',
                       'CompositorNodeDenoise',
                       'CompositorNodeOutputFile']}

    created_slots = []

    settings = Settings()

    def __init__(self):
        return

    def layer_name(self):
        layer_name = bpy.context.window.view_layer.name
        return layer_name

    def layer_node_to_scene(self, scene, layer_name):
        self.enable_nodes(scene)
        bpy.context.window.scene = scene
        update_scene = bpy.context.window.scene
        return_value = None
        if update_scene.view_layers[layer_name]:
            for node in scene.node_tree.nodes:
                try:
                    if node.layer != layer_name:
                        render_layer_node = self.create_layer_node(
                            update_scene)
                        render_layer_node.layer = layer_name
                        return_value = render_layer_node
                    else:
                        return_value = node
                except Exception as e:
                    print("Trying to create Render Layer Node, but ERROR: ", e)
        return return_value

    def create_slots(self, scene, layer_name, prop_group):
        self.enable_nodes(scene)
        for pass_name in prop_group:
            if prop_group.get(pass_name):
                slot_name = scene.name + "_" + layer_name + '_' + pass_name
                slot_name_full = slot_name + "/" + slot_name + "_"
                if not slot_name_full in self.created_slots:
                    output_node = scene.node_tree.nodes['File Output']
                    slot = output_node.file_slots.new(slot_name_full)
                    self.created_slots.append(slot_name_full)

    def link_nodes(self, scene):

        render_layer_node_type = 'R_LAYERS'
        output_node_type = 'OUTPUT_FILE'

        self.enable_nodes(scene)

        nodes = scene.node_tree.nodes
        links = scene.node_tree.links
        output_node = nodes['File Output']

        for node in nodes:
            if node.type == render_layer_node_type:

                for key in node.outputs.keys():
                    for socket in output_node.inputs.keys():
                        ssocket_string_list = socket.split('_')
                        layer_name = ssocket_string_list[-3]
                        pass_name = ssocket_string_list[-2]

                        if node.layer == layer_name:

                            if key == pass_name:
                                links.new(
                                    node.outputs[key], output_node.inputs[socket])

    def create_denoise_node(self, scene):
        denoise_node = scene.node_tree.nodes.new(
            type="CompositorNodeDenoise")
        return denoise_node

    def link_layer_to_denoise(self, scene, layer_node, denoise_node):
        print("DEBUG: link_layer_to_denoise()")
        print("DEBUG:", layer_node)
        output_node = scene.node_tree.nodes['File Output']
        links = scene.node_tree.links
        links.new(layer_node.outputs['Noisy Image'], denoise_node.inputs[0])
        links.new(
            layer_node.outputs['Denoising Normal'], denoise_node.inputs['Normal'])
        links.new(
            layer_node.outputs['Denoising Albedo'], denoise_node.inputs['Albedo'])
# Get Last name
        for socket in output_node.inputs.keys():
            ssocket_string_list = socket.split('_')
            layer_name = ssocket_string_list[-3]
            pass_name = ssocket_string_list[-2]

            if pass_name == "Denoise":
                links.new(
                    denoise_node.outputs['Image'], output_node.inputs[socket])

    def enable_nodes(self, scene):
        if not scene.use_nodes:
            scene.use_nodes = True
            self.create_file_output_node(scene)

    def create_layer_node(self, scene):
        node = scene.node_tree.nodes.new(
            type="CompositorNodeRLayers")
        return node

    def create_file_output_node(self, scene):
        output_node = scene.node_tree.nodes.new(
            type="CompositorNodeOutputFile")
        output_node.file_slots.clear()
        output_node.base_path = self.settings.get_relative_render_path()

    def clear_slots(self, scene):
        self.enable_nodes(scene)
        scene.node_tree.nodes["File Output"].file_slots.clear()
