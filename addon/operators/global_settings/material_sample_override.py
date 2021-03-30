import bpy


class OLV_OP_Material_Sample_Overrides():
    bl_idname = "olv.op_material_sample_overrides"
    bl_label = "Render layer material sample overrides"

    material_samples = bpy.props.IntProperty(default=0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        # print("OLV_OP_Layer_Material_Overrides MATERIAL: ", self.material_name)

        # for scene in bpy.data.scenes:
        #     for layer in scene.view_layers:
        #         if layer.name == bpy.context.view_layer.name:
        #             layer.samples = self.material_samples

        return{'FINISHED'}

    def get_samples(self, context):
        return self.material_samples

# bpy.context.scene.view_layers["View Layer"].material_override = bpy.data.materials["Material"]
