import bpy
from ..properties.projects_on_disk import OLV_P_Projects_On_Disk


class OLV_MT_Project_List_Menu(bpy.types.Menu):
    bl_idname = 'olv.project_list_menu'
    bl_label = 'Project List'
    projects_on_disk = OLV_P_Projects_On_Disk()


    def draw(self, context):
        projects = self.projects_on_disk.get_projects()

        layout = self.layout

        for project in projects:
            lo = layout.operator('olv.save_project_file',
                                 text=project, icon='RADIOBUT_ON')
            
            
            # row = layout.row(align=True)
            # col = row.column(align=True)
            # lo.prop()
