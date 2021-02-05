import os
import json
from ..utility.settings import Settings


class OLV_P_Projects_On_Disk():

    settings = Settings()
    
    def get_projects(self):
        path = self.settings.get_x_drive_path()
        projects = os.listdir(path=path)
        return os.listdir(path=path)
