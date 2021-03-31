import json
from pathlib import Path
import bpy


class Settings:

    settings_file = Path(__file__).absolute(
    ).parent.parent.parent / "settings.json"

    def get_x_drive_path(self):
        return self.open_settings("Xdrive path")

    def get_assets_path(self):
        return self.open_settings("Assets path")

    def get_relative_render_path(self, scene_name):
        blender_file_name = self.get_blender_file_name() + "/" + scene_name
        base_path = self.open_settings(
            "Render Path") + blender_file_name + "/"
        # return self.open_settings("Render Path")
        return base_path

    def get_nodes(self):
        return self.open_settings("Nodes")

    def open_settings(self, settings_key):
        with open(self.settings_file) as my_file:
            value = json.load(my_file).get(settings_key)
        return value

    def get_blender_file_name(self):
        file_name = bpy.path.basename(bpy.context.blend_data.filepath)
        file_name = file_name.split(".")
        file_name = file_name[0]

        if not file_name == "":
            return file_name
        else:
            return "BlenderFileNotSaved"
