import bpy


class OLV_OP_Bulk_Suffix(bpy.types.Operator):

    bl_idname = 'olv.op_bulk_suffix'
    bl_label = 'Bulk rename'

    suffix = bpy.props.StringProperty(default='')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        for selected_object in bpy.context.selected_objects:
            selected_object.name = selected_object.name + '_' + self.suffix

        return {'FINISHED'}
