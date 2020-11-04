import bpy


class OLV_MT_Name_New_Project_Menu(bpy.types.Menu):
    bl_name = 'OLV_MT_Name_New_Project_Menu'
    bl_label = 'OLV New Project'

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        # row = layout.row()
        # layout.label(text='new_project_label')
        # project_name = bpy.props.StringProperty(name='project name', default='')
        layout.operator('olv.create_new_project',
                        text='New Project', emboss=False, icon='FILE')
