import bpy


class CreateCompNodes():
    bl_name = 'olv.create_comp_nodes'
    bl_label = 'Create comp nodes for rendering'

    operator = bpy.ops

    nodes = {'Nodes': ['CompositorNodeRLayers',
                       'CompositorNodeDenoise',
                       'CompositorNodeOutputFile']}

    def __init__(self):
        return

    def layer_name(self):
        layer_name = bpy.context.window.view_layer.name
        return layer_name

    def create_layer_node(self, scene, layer_name):

        bpy.context.window.scene = scene
        update_scene = bpy.context.window.scene
        if update_scene.view_layers[layer_name]:
            for node in scene.node_tree.nodes:
                try:
                    if node.layer != layer_name:
                        render_layer_node = update_scene.node_tree.nodes.new(
                            type="CompositorNodeRLayers")
                        render_layer_node.layer = layer_name
                except Exception as e:
                    print("Trying to create Render Layer Node, but ERROR: ", e)

    def create_slots(self, scene, layer_name, pass_name):
        slot_name = scene.name + "_" + layer_name + '_' + pass_name
        slot_name_full = slot_name + "/" + slot_name + "_"

        output_node = scene.node_tree.nodes['File Output']

        output_node.file_slots.new(slot_name_full)

    def link_layer_to_denoise(self, layer, denoise, output):
        links = bpy.context.scene.node_tree.links
        links.new(layer.outputs['Noisy Image'], denoise.inputs[0])
        links.new(layer.outputs['Denoising Normal'], denoise.inputs['Normal'])
        links.new(layer.outputs['Denoising Albedo'], denoise.inputs['Albedo'])

        links.new(denoise.outputs['Image'], output.inputs[self.slot_name()])

    def link_nodes(self):

        scenes = bpy.data.scenes

        render_layer_node_type = 'R_LAYERS'
        output_node_type = 'OUTPUT_FILE'

        render_node_outputs = []

        for scene in scenes:
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
                                    print("KEY: ", key, "PASS NAME:", pass_name)
                                    links.new(
                                        node.outputs[key], output_node.inputs[socket])
