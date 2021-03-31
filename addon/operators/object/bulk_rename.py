import bpy


class OLV_OP_Bulk_Rename(bpy.types.Operator):

    bl_name = 'olv.op_bulk_rename'
    bl_label = 'Bulk rename'

    operation = bpy.props.StringProperty(default='rename')

    options = ['rename', 'suffix', 'prefix']

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        return {'FINISHED'}
