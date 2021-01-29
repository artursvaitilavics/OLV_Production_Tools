import bpy
from ..properties.projects_on_disk import OLV_P_Projects_On_Disk
# from ..operators.save_project_file import OLV_OP_Save_Project_File


class OLV_MT_Project_List_Menu(bpy.types.Menu):
    bl_idname = 'olv.project_list_menu'
    bl_label = 'Project List'
    projects_on_disk = OLV_P_Projects_On_Disk()

    # project_name = OLV_OP_Save_Project_File()

    def draw(self, context):
        projects = self.projects_on_disk.get_projects()

        layout = self.layout

        for project in projects:

            # self.project_name(project)

            lo = layout.operator('olv.save_project_file',
                                 text=project, icon='RADIOBUT_ON')
            lo.project_name = project

            # row = layout.row(align=True)P
            # col = row.column(align=True)P
            # lo.prop()
