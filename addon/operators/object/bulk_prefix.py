import bpy


class OLV_OP_Bulk_Prefix(bpy.types.Operator):

    bl_idname = 'olv.op_bulk_prefix'
    bl_label = 'Bulk rename'

    prefix = bpy.props.StringProperty(default='')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        for selected_object in bpy.context.selected_objects:
            selected_object.name = self.prefix + '_' + selected_object.name

        return {'FINISHED'}
