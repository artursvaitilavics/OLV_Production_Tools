import bpy
import os
import json
from pathlib import Path

from ..utility.settings import Settings


class OLV_OP_Create_New_Project(bpy.types.Operator):
    bl_idname = 'olv.create_new_project'
    bl_label = 'Create New Project'

    get_path = Settings()

    x_drive_path = get_path.get_x_drive_path()

    # TODO: Curently hard coded, to be replaced with json
    sub_dir_00 = {'00_References': [
        '01_From_Client', '02_Local', '03_From_SEA']}
    sub_dir_01 = {'01_Concepts': ['01_Sketches', '02_Provided']}
    sub_dir_02 = {'02_Assets': ['01_From_Client', '02_3D', '03_2D']}
    sub_dir_03 = {'03_Production': ['01_3D', '02_AE']}
    sub_dir_04 = {'04_Output': ['01_Crisp', '02_Review']}
    sub_dir_05 = {'05_Temp': []}

    # TODO: Create method that will add all subdirs from json file
    sub_directories = [sub_dir_00, sub_dir_01,
                       sub_dir_02, sub_dir_03, sub_dir_04, sub_dir_05]

    root_directory = bpy.props.StringProperty(
        name='Project Name', default='')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        directory = self.x_drive_path + self.root_directory

        try:
            os.mkdir(directory)
            for sub_dir in self.sub_directories:
                self.create_directories(sub_dir)
            return {'FINISHED'}
        except:
            print("Can't make project")
        return {'FINISHED'}

    def create_directories(self, directories: {}):
        directory = self.x_drive_path + self.root_directory
        for items in directories:
            directory = directory + '/' + items
            temp_directory = directory
            os.mkdir(directory)
            for sub_item in directories.get(items):
                directory = directory + '/' + sub_item
                os.mkdir(directory)
                directory = temp_directory
