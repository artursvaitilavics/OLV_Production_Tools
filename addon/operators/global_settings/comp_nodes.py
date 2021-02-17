import bpy
from ...utility.settings import Settings


class CompNodes:

    settings = Settings()

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
            scene.node_tree.nodes[self.output_node_name].file_slots.new(
                "TEST_SLOT")


# save all passes in seperate temp json
# when creating slots, read from this json, (later do this also for applying settings)
# Helper Methods

    def __create_slot(self, scene):
        scene.node_tree.nodes[self.output_node_name].file_slots.new(
                "TEST_SLOT")


    def __get_view_layers(self, scene):
        layer_names = []
        for layer in scene.view_layers:
            layer_names.append[layer.name]
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
