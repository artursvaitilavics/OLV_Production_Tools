import bpy
from ...properties.suffix_prefix_update import SuffixPrefixUpdate


class OLV_OP_Bulk_Suffix(bpy.types.Operator):

    bl_idname = 'olv.op_bulk_suffix'
    bl_label = 'Bulk rename'

    suffix = bpy.props.StringProperty(default='')
    change_suffix = bpy.props.BoolProperty(default=False)

    update = SuffixPrefixUpdate()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if self.change_suffix:
            self.replace_suffix(self.suffix)
        else:
            self.add_suffix(self.suffix)
        return {'FINISHED'}

    def add_suffix(self, suffix):
        for selected_object in bpy.context.selected_objects:
            name_number = self.update.seperate_name_from_number(
                selected_object.name)
            if len(name_number) > 1:
                selected_object.name = name_number[0] + \
                    '_' + suffix + '.' + name_number[1]
            else:
                selected_object.name = name_number[0] + '_' + suffix

    def replace_suffix(self, suffix):
        for selected_object in bpy.context.selected_objects:
            seperated = self.update.fix_suffix(selected_object.name)
            name = seperated.get('name')
            old_suffix = seperated.get('suffix')
            number = seperated.get('number')
            print("NAME:", name)
            print("OLD_SUFFIX:", name)
            print("NEW SUFFIX:", suffix)
            print("NAME:", name)
            if number != '':
                selected_object.name = name + '_' + suffix + '.' + number
            else:
                selected_object.name = name + '_' + suffix
