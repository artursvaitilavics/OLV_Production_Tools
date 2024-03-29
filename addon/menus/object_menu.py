import bpy


class OLV_MT_Object_Menu(bpy.types.Menu):
    bl_idname = 'olv.object_menu'
    bl_label = 'Object Menu'

    def draw(self, context):
        layout = self.layout

        layout.operator('olv.link_object_to_all_scenes',
                        text='Link to all scenes', icon='LINKED')

        layout.menu('olv.mt_bulk_rename', text='Rename')