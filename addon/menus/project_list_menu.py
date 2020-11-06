import bpy


class OLV_MT_Project_List_Menu(bpy.types.Menu):
    bl_idname = 'olv.project_list_menu'
    bl_label = 'Project List'

    def draw(self, context):
        layout = self.layout

        from ..properties.projects_on_disk import OLV_P_Projects_On_Disk

        projects_on_disk = OLV_P_Projects_On_Disk()

        for project in projects_on_disk.get_projects():
            lo = layout.operator('olv.save_project_file',
                                 text=project, icon='RADIOBUT_ON')
            lo.project_name = project