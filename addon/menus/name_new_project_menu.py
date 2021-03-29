import bpy


class OLV_MT_Name_New_Project_Menu(bpy.types.Menu):
    bl_name = 'OLV_MT_Name_New_Project_Menu'
    bl_label = 'OLV New Project'

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        layout.operator('olv.create_project_file',
                        text='Set Project File', icon='FILE')
        layout.operator('olv.create_new_project',
                        text='New Project', emboss=False, icon='FILEBROWSER')
        layout.menu('olv.project_list_menu',
                    text='Save File', icon='FILE_TICK')
