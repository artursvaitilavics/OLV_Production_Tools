import bpy


class CreateCompNodes():
    bl_name = 'olv.create_comp_nodes'
    bl_label = 'Create comp nodes for rendering'

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
            render_layer_node = update_scene.node_tree.nodes.new(
                type="CompositorNodeRLayers")
            render_layer_node.layer = layer_name
