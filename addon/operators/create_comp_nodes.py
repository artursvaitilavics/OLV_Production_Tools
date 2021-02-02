import bpy


class CreateCompNodes():
    bl_name = 'olv.create_comp_nodes'
    bl_label = 'Create comp nodes for rendering'

    operator = bpy.ops

    # TODO: Create nodes for each view layer, and for enabled passes
    nodes = {'Nodes': ['CompositorNodeRLayers',
                       'CompositorNodeDenoise',
                       'CompositorNodeOutputFile']}

    def __init__(self):
        return

    def sayHi(self):
        print(
            '----------------------------------------------Create Comp Nodes saying Hello!')

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
        scene.node_tree.nodes['File Output'].file_slots.new(
            slot_name + "/" + slot_name + "_")

    def enable_nodes(self):
        for scene in bpy.data.scenes:
            bpy.context.window.scene = scene
            scene.use_nodes = True
            nodes = scene.node_tree.nodes
            self.create_nodes(nodes)
            self.create_output_file_slots(nodes['File Output'])
            self.link_layer_to_denoise(
                nodes['Render Layers'], nodes['Denoise'], nodes['File Output'])

    def create_nodes(self, nodes):

        x_pos = 0
        y_pos = 0

        nodes.clear()

        for node in self.nodes.get('Nodes'):
            if not node:
                new_node = nodes.new(node)
                new_node.location.x = x_pos
                x_pos += 500

    def link_layer_to_denoise(self, layer, denoise, output):
        links = bpy.context.scene.node_tree.links
        links.new(layer.outputs['Noisy Image'], denoise.inputs[0])
        links.new(layer.outputs['Denoising Normal'], denoise.inputs['Normal'])
        links.new(layer.outputs['Denoising Albedo'], denoise.inputs['Albedo'])

        links.new(denoise.outputs['Image'], output.inputs[self.slot_name()])

    def create_output_file_slots(self, node):
        node.base_path = '//../../02_Assets/02_3D/'
        node.file_slots.clear()
        slot = node.file_slots.new(self.slot_name())

    def slot_name(self):
        scene_name = bpy.context.scene.name
        render_layer = 'img'
        slot_description = scene_name + '_' + render_layer
        return slot_description + '/' + slot_description + '_'
