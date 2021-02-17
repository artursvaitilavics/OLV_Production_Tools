import bpy
from ...utility.settings import Settings

# TODO: refactor this so it is reusable for various needs


class OLV_OP_Create_Output_Nodes():
    bl_idname = 'olv.create_output_nodes'
    bl_label = 'Create output nodes'

    operator = bpy.ops

    settings = Settings()

    def execute(self):
        self.enable_nodes()
        return{'FINISHED'}

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

        
        for node in self.settings.get_nodes():

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
        # TODO: replace path with settings relative path
        node.base_path = self.settings.get_relative_render_path()
        # node.base_path = '//../../02_Assets/02_3D/'
        node.file_slots.clear()
        slot = node.file_slots.new(self.slot_name())

    def slot_name(self):
        scene_name = bpy.context.scene.name
        render_layer = 'img'
        slot_description = scene_name + '_' + render_layer
        return slot_description + '/' + slot_description + '_'
