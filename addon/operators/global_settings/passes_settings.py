import json
from pathlib import Path


class PassesSettings:

    settings_file = Path(__file__).absolute(
    ).parent / "passes_settings.json"


    def get_image(self):
        return self.open_settings("Image")

    def get_all_passes(self):
        with open(self.settings_file) as my_file:
            value = json.load(my_file)
        return value

    def open_settings(self, settings_key):
        with open(self.settings_file) as my_file:
            value = json.load(my_file).get(settings_key)
        return value


# settings = Settings()

# result = settings.get_all_passes()

# for render_pass in result:
#     print(render_pass)