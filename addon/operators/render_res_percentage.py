import bpy


class OLV_OP_Set_Resolution_Percentage(bpy.types.Operator):
    bl_idname = 'olv.set_resolution_percentage'
    bl_label = 'Set Resolution Percentage'

    resolution_percentage = bpy.props.IntProperty(name='Resolution %', default=100)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        for scene in bpy.data.scenes:
            scene.render.resolution_percentage = self.resolution_percentage
        return {'FINISHED'}
