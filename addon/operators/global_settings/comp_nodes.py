import bpy
from ...utility.settings import Settings
from .passes_settings import PassesSettings
from .active_render_passes import ActiveRenderPasses


class CompNodes:

    settings = Settings()
    passes_settings = PassesSettings()
    active_render_passes = ActiveRenderPasses()

    output_node_name = "File Output"
    render_layer_node_type = "R_LAYERS"

    def create_layers(self):
        for scene in bpy.data.scenes:
            for layer in scene.view_layers:
                node = self.__create_layer_node(scene)
                node.scene = scene
                node.layer = layer.name

    def create_file_output(self):
        for scene in bpy.data.scenes:
            self.__create_file_output_node(scene)

    def enable_nodes(self):
        for scene in bpy.data.scenes:
            if not scene.use_nodes:
                scene.use_nodes = True
                scene.node_tree.nodes.clear()

    def create_slots(self):
        for scene in bpy.data.scenes:
            scene.node_tree.nodes[self.output_node_name].file_slots.clear()

            for view_layer in scene.view_layers:
                # ___NOTE____ get dictionary with all passes in all scnes and all view layers
                passes = self.active_render_passes.set_passes(view_layer)

                for key in passes:
                    if passes[key]:
                        # Here we can finaly create slots!!!! LIKE A MOZA FOKA
                        socket = self.__create_slot(
                            scene, view_layer.name, key)

    def create_links(self):

        for scene in bpy.data.scenes:
            links = scene.node_tree.links
            output_node = scene.node_tree.nodes[self.output_node_name]
            for node in scene.node_tree.nodes:

                if node.type == self.render_layer_node_type:
                    denoise_to_create = []

                    for key in node.outputs.keys():
                        for socket in output_node.inputs.keys():
                            ssocket_string_list = socket.split('_')
                            layer_name = ssocket_string_list[-3]
                            pass_name = ssocket_string_list[-2]

                            if node.layer == layer_name:
                                if key == pass_name:
                                    links.new(
                                        node.outputs[key], output_node.inputs[socket])

# Bellow stuff in function should be seperated from here and connect new denoise to input slot in file output node
                                if key == "Denoising Normal" and pass_name == "Denoise" and layer_name == node.layer:
                                    # Make only as many Denoise nodes, as needed! Currently too shitty
                                    denoise_node = self.__create_denoise_node(
                                        scene)
                                    self.__link_denoise_node(
                                        scene, node, denoise_node, output_node)

    def __create_slot(self, scene, view_layer_name, render_pass_name):
        combined_name = scene.name + "_" + view_layer_name + "_" + render_pass_name
        slot_name = combined_name + "/" + combined_name + "_"
        node = scene.node_tree.nodes[self.output_node_name]
        # node.file_slots.clear()
        node.file_slots.new(
            slot_name)

    def __get_view_layers(self, scene):
        layer_names = []
        for layer in scene.view_layers:
            layer_names.append(layer.name)
        return layer_names

    def __create_layer_node(self, scene):
        node = scene.node_tree.nodes.new(
            type="CompositorNodeRLayers")
        return node

    def __create_file_output_node(self, scene):
        output_node = scene.node_tree.nodes.new(
            type="CompositorNodeOutputFile")

    def __create_denoise_node(self, scene):
        denoise_node = scene.node_tree.nodes.new(type="CompositorNodeDenoise")
        return denoise_node

    def __link_denoise_node(self, scene, layer_node, denoise_node, output_node):
        # output_node = scene.node_tree.nodes[self.output_node_name]
        print(scene.name, layer_node.name, denoise_node.name, output_node.name)
        links = scene.node_tree.links
        links.new(layer_node.outputs['Noisy Image'], denoise_node.inputs[0])
        links.new(layer_node.outputs['Denoising Normal'],
                  denoise_node.inputs['Normal'])
        links.new(layer_node.outputs['Denoising Albedo'],
                  denoise_node.inputs['Albedo'])

        socket = self.__get_socket_pass_name(output_node)

        links.new(denoise_node.outputs['Image'], output_node.inputs[socket])

    def __get_socket_pass_name(self, output_node):
        return_value = ""
        for socket in output_node.inputs.keys():
            ssocket_string_list = socket.split('_')
            layer_name = ssocket_string_list[-3]
            pass_name = ssocket_string_list[-2]
            if pass_name == "Denoise":
                return_value = socket
            else:
                return_value == ""
        return return_value

    def clear_node_tree(self):

        for scene in bpy.data.scenes:
            try:
                scene.node_tree.nodes.clear()
            except:
                print("No nodes to clear...")

    def set_relative_render_path(self):
        for scene in bpy.data.scenes:
            for node in scene.node_tree.nodes:
                if node.name == self.output_node_name:
                    node.base_path = self.settings.get_relative_render_path()

