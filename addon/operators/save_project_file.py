import bpy
import json
from ..utility.settings import Settings
import os
import glob

# TODO: cahnge bellow class to use settings.py module
from ..properties.projects_on_disk import OLV_P_Projects_On_Disk


class OLV_OP_Save_Project_File(bpy.types.Operator):
    bl_idname = 'olv.save_project_file'
    bl_label = 'Save Project File'

    xdrive = Settings()

    project_name = bpy.props.StringProperty(default='Arturs_Project')

    prod_dir_path = '/03_PRODUCTION/3D/'

    def execute(self, context):
        curent_version = self.get_version_from_dir(self.project_name)
        new_version = self.increment_version(curent_version)
        self.save_project_file(self.project_name, new_version)
        return {'FINISHED'}

    def save_project_file(self, project_name, version):
        path = self.xdrive.get_x_drive_path()
        # path_part_2 = '/03_PRODUCTION/3D/'
        bpy.ops.wm.save_as_mainfile(
            filepath=path + project_name + self.prod_dir_path + project_name + '_' + version + '.blend')

    def increment_version(self, version_number):
        version_number = version_number + 1

        if version_number <= 9:
            return "00" + str(version_number)
        elif version_number <= 99:
            return "0" + str(version_number)
        else:
            return str(version_number)

    def get_version_from_dir(self, project_name):
        project_path = self.xdrive.get_x_drive_path() + project_name + \
            self.prod_dir_path
        project_files = os.listdir(project_path)

        all_blend_files = []

        for file in glob.glob(project_path + "*.blend"):
            all_blend_files.append(file)

        highest_version_name = max(all_blend_files)

        version = highest_version_name.split(".")

        version_number = int(version[0].split("_")[-1])

        return version_number
