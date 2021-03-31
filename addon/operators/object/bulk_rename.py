import bpy


class OLV_OP_Bulk_Rename(bpy.types.Operator):

    bl_idname = 'olv.op_bulk_rename'
    bl_label = 'Bulk rename'

    name = bpy.props.StringProperty(default='')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        counter = 1
        for selected_object in bpy.context.selected_objects:
            selected_object.name = self.name + '_' + str(counter)
            counter = counter + 1

        return {'FINISHED'}
