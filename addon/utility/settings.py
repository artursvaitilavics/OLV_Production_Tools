import json
from pathlib import Path


class Settings:

    settings_file = Path(__file__).absolute(
    ).parent.parent.parent / "settings.json"

    def get_x_drive_path(self):
        return self.open_settings("Xdrive path")

    def get_assets_path(self):
        return self.open_settings("Assets path")

    def get_relative_render_path(self):
        return self.open_settings("Render Path")

    def get_nodes(self):
        return self.open_settings("Nodes")

    def open_settings(self, settings_key):
        with open(self.settings_file) as my_file:
            value = json.load(my_file).get(settings_key)
        return value
