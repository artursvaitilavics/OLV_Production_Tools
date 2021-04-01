import bpy
from ...properties.suffix_prefix_update import SuffixPrefixUpdate


class OLV_OP_Bulk_Prefix(bpy.types.Operator):

    bl_idname = 'olv.op_bulk_prefix'
    bl_label = 'Bulk rename'

    new_prefix = bpy.props.StringProperty(default='')
    old_prefix = bpy.props.StringProperty(default='')
    replace_prefix = bpy.props.BoolProperty(default=False)
    

    update = SuffixPrefixUpdate()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if self.replace_prefix:
            self.rename_prefix(self.old_prefix, self.new_prefix)
        else:
            self.add_prefix(self.new_prefix)

        self.new_prefix = ''
        self.old_prefix = ''
        self.replace_prefix = False
        return {'FINISHED'}

    def add_prefix(self, prefix):
        for selected_object in bpy.context.selected_objects:
            selected_object.name = prefix + '_' + selected_object.name

    def rename_prefix(self, old_prefix, new_prefix):
        for selected_object in bpy.context.selected_objects:
            selected_object.name = self.update.fix_prefix(
                selected_object.name, new_prefix, old_prefix)
