import os
import json


class OLV_P_Projects_On_Disk():
    # path = '../../x_disk_system_link/'   # This works in this file localy
    # path = 'x_disk_system_link/'

    with open('./settings.json') as my_file:
        settings_data = json.load(my_file)
        path = settings_data.get("Xdrive path")

    projects = os.listdir(path=path)

    def get_projects(self):
        return os.listdir(path=self.path)


print(OLV_P_Projects_On_Disk().get_projects())
