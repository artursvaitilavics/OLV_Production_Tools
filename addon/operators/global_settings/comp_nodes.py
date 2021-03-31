import bpy
from ...utility.settings import Settings
from .passes_settings import PassesSettings
from .active_render_passes import ActiveRenderPasses
from .parse_sockets import ParseSockets


class CompNodes:

    settings = Settings()
    passes_settings = PassesSettings()
    active_render_passes = ActiveRenderPasses()

    output_node_name = "File Output"
    render_layer_node_type = "R_LAYERS"

    parse_sockets = ParseSockets()

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
                        socket = self.__create_slot(scene,
                                                    view_layer.name, key)

    def create_links(self):

        for scene in bpy.data.scenes:
            links = scene.node_tree.links
            output_node = scene.node_tree.nodes[self.output_node_name]
            for node in scene.node_tree.nodes:

                if node.type == self.render_layer_node_type:

                    for key in node.outputs.keys():

                        for socket in output_node.inputs.keys():
                            if self.__layer(socket, node.layer) and self.__pass(socket, key):
                                links.new(
                                    node.outputs[key], output_node.inputs[socket])

# REBUILD view_layer/pass
    def __create_slot(self, scene, view_layer_str, render_pass_name):
        view_layer_name = view_layer_str
        combined_name = view_layer_name + "/" + render_pass_name + "_"
        # slot_name = combined_name + "/" + combined_name + "_"
        node = scene.node_tree.nodes[self.output_node_name]
        node.file_slots.new(
            combined_name)

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

    def __create_denoise_node(self, scene, render_layer_node):
        for output in render_layer_node.outputs.keys():
            if output == "Denoising Normal":
                denoise_node = scene.node_tree.nodes.new(
                    type="CompositorNodeDenoise")
                return denoise_node

    def __link_denoise_node(self, scene, layer_node, denoise_node, socket):
        try:
            output_node = scene.node_tree.nodes[self.output_node_name]
            links = scene.node_tree.links
            links.new(
                layer_node.outputs['Noisy Image'], denoise_node.inputs[0])
            links.new(layer_node.outputs['Denoising Normal'],
                      denoise_node.inputs['Normal'])
            links.new(layer_node.outputs['Denoising Albedo'],
                      denoise_node.inputs['Albedo'])
            links.new(denoise_node.outputs['Image'],
                      output_node.inputs[socket])
        except:
            print("EXCEPTION: Can't create denoise links...")

    def __get_socket_pass_name(self, output_node):
        return_value = ""
        for socket in output_node.inputs.keys():
            ssocket_string_list = socket.split('/')
            layer_name = ssocket_string_list[0]
            pass_value = ssocket_string_list[1]
            pass_name = pass_value.split('_')
            pass_name = pass_name[0]
            if pass_name == "Denoise":
                return_value = socket
            else:
                return_value == ""
        return return_value
    # def __get_socket_pass_name(self, output_node):
    #         return_value = ""
    #     for socket in output_node.inputs.keys():
    #         ssocket_string_list = socket.split('_')
    #         layer_name = ssocket_string_list[-3]
    #         pass_name = ssocket_string_list[-2]
    #         if pass_name == "Denoise":
    #             return_value = socket
    #         else:
    #             return_value == ""
    #     return return_value

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
                    # ------------ Seting base Path
                    node.base_path = self.settings.get_relative_render_path(
                        scene.name)

    def __get_socket(self, socket):
        return self.parse_sockets.clean_socket(socket).get(("socket"))

    def __pass(self, socket, required_pass):
        return self.parse_sockets.clean_socket(socket).get("pass") == required_pass

    def __layer(self, socket, required_layer):
        return self.parse_sockets.clean_socket(socket).get("layer") == required_layer

    def __get_render_layer_nodes(self):
        render_layer_nodes = []
        for scene in bpy.data.scenes:
            print("SCENE:", scene.name)
            for node in scene.node_tree.nodes:
                if node.type == self.render_layer_node_type:
                    render_layer_nodes.append(node)
        return render_layer_nodes

    def new_cretae_denoise_nodes(self):
        render_layer_nodes = self.__get_render_layer_nodes()

        for render_layer_node in render_layer_nodes:
            render_layer_node.scene.node_tree.links.new()
            print(render_layer_node.scene.name)

    def link_denoise(self):
        for scene in bpy.data.scenes:
            output_node = scene.node_tree.nodes[self.output_node_name]
            links = scene.node_tree.links
            for node in scene.node_tree.nodes:
                if node.type == self.render_layer_node_type:
                    layer_node = node
                    node_layer = layer_node.layer
                    print(node_layer)

                    for socket in output_node.inputs:
                        is_layer = self.__layer(socket.name, node_layer)
                        is_pass = self.__pass(socket.name, "Denoise")

                        if is_layer and is_pass:
                            denoise_node = scene.node_tree.nodes.new(
                                type="CompositorNodeDenoise")

                            try:
                                links.new(
                                    layer_node.outputs['Noisy Image'], denoise_node.inputs[0])
                                links.new(layer_node.outputs['Denoising Normal'],
                                          denoise_node.inputs['Normal'])
                                links.new(layer_node.outputs['Denoising Albedo'],
                                          denoise_node.inputs['Albedo'])
                                links.new(denoise_node.outputs['Image'],
                                          output_node.inputs[socket.name])
                            except:
                                print("EXCEPTION: Can't create denoise links...")
