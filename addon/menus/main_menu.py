import bpy

from .name_new_project import OLV_MT_Name_New_Project_Menu


class OLV_MT_Main_Menu(bpy.types.Menu):
    bl_idname = 'OLV_MT_Main_Menu'
    bl_label = 'OLV Main Menu'

    def draw(self, context):
        layout = self.layout
        # layout.operator_context = 'INVOKE_DEFAULT'
        # layout.label(text = 'OLV Tools')

        layout.menu('OLV_MT_Name_New_Project_Menu',
                    text='Project', icon='OUTLINER_OB_LATTICE')
