import bpy
import json

from ..properties.projects_on_disk import OLV_P_Projects_On_Disk


class OLV_OP_Save_Project_File(bpy.types.Operator):
    bl_idname = 'olv.save_project_file'
    bl_label = 'Save Project File'

    # projects = OLV_P_Projects_On_Disk()
    project_name = bpy.props.StringProperty(default='Arturs_Project')

    # def __init__(self, name):
    #     self.project_name = name
        #  bpy.props.StringProperty(default='Arturs_Project')

    def execute(self, context):
        self.save_project_file(self.project_name)
        print(self.project_name)
        return {'FINISHED'}

    def save_project_file(self, project_name: str):

        with open('./settings.json') as my_file:
            settings_data = json.load(my_file)
            path = settings_data.get("Xdrive path")

        # path = 'x_disk_system_link/'
        path_part_2 = '/03_Production/01_3D/'
        version = 1  # TODO: make dynamic
        bpy.ops.wm.save_as_mainfile(
            filepath=path + project_name + path_part_2 + project_name + '_' + str(version) + '.blend')
