import bpy


class OLV_MT_Bulk_Rename(bpy.types.Menu):

    bl_idname = 'olv.mt_bulk_rename'
    bl_label = 'Bulk rename'

    options = ['rename', 'add suffix', 'add prefix']

    def draw(self, context):
        layout = self.layout
        lo = layout.operator('olv.op_bulk_rename', text='rename selected')
        suffix_layout = layout.operator(
            'olv.op_bulk_suffix', text='add suffix to selected')
        prefix_layout = layout.operator(
            'olv.op_bulk_prefix', text='add prefix to selected')

        # for option in self.options:
        #     lo = layout.operator('olv.op_bulk_rename', text=option)
        # lo.operation = option
