import bpy

from .material_sample_override import OLV_OP_Material_Sample_Overrides


class OLV_OP_Layer_Material_Overrides(bpy.types.Operator):
    bl_idname = "olv.op_layer_material_overrides"
    bl_label = "Render layer material overrides"

    material_name = bpy.props.StringProperty(default="default value")
    material_samples = bpy.props.IntProperty(default=0)

    # mat_sample = OLV_OP_Material_Sample_Overrides()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        print("OLV_OP_Layer_Material_Overrides MATERIAL: ", self.material_name)

        # samples = self.mat_sample.get_samples(context)

        for scene in bpy.data.scenes:
            for layer in scene.view_layers:
                if layer.name == bpy.context.view_layer.name:
                    layer.material_override = bpy.data.materials[self.material_name]
                    layer.samples = self.material_samples

                    

        return{'FINISHED'}


# bpy.context.scene.view_layers["View Layer"].material_override = bpy.data.materials["Material"]
