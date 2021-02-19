import bpy
from ...utility.settings import Settings
from .passes_settings import PassesSettings
from .active_render_passes import ActiveRenderPasses


class CompNodes:

    settings = Settings()
    passes_settings = PassesSettings()
    active_render_passes = ActiveRenderPasses()

    output_node_name = "File Output"

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
            for view_layer in scene.view_layers:
                print(scene.name, view_layer.name)
        # for scene in bpy.data.scenes:
        #     for view_layer in scene.view_layers:
        #         image = view_layer.use_pass_combined
        #         print(scene.name, view_layer.name, image)
        # self.__slots_to_create(scene)
        # node = scene.node_tree.nodes[self.output_node_name]
        # node.file_slots.clear()
        # for layer_name in self.__get_view_layers(scene):
        #     for render_pass in render_passes:
        #         slot_name = layer_name + "/" + render_pass + "_"
        #         node.file_slots.new(slot_name)


# TODO: eval(render_settings.get(render_setting))   GET THIS DO SOME MAGIC


    def __slots_to_create(self, scene):
        image = self.active_render_passes.active_passes(scene).get('Image')
        print(scene.name, image)

    def __create_slot(self, scene, render_pass):
        node = scene.node_tree.nodes[self.output_node_name]
        node.file_slots.clear()
        node.file_slots.new(
            render_pass)

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

    def reference_create_slots(self, scene, layer_name, prop_group):
        self.enable_nodes(scene)
        for pass_name in prop_group:
            if prop_group.get(pass_name):
                slot_name = scene.name + "_" + layer_name + '_' + pass_name
                slot_name_full = slot_name + "/" + slot_name + "_"
                if not slot_name_full in self.created_slots:
                    output_node = scene.node_tree.nodes['File Output']
                    slot = output_node.file_slots.new(slot_name_full)
                    self.created_slots.append(slot_name_full)

    def __create_slot(self, name):
        name = "TEST"
