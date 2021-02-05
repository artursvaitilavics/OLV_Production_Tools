import json
from pathlib import Path


class Settings:

    settings_file = Path(__file__).absolute(
    ).parent.parent.parent / "settings.json"

    def get_x_drive_path(self):

        with open(self.settings_file) as my_file:
            xdrive_path = json.load(my_file).get("Xdrive path")
        return xdrive_path

    def get_assets_path(self):
        with open(self.settings_file) as my_file:
            assets_path = json.load(my_file).get("Assets path")
        return assets_path

