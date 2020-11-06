import os


class OLV_P_Projects_On_Disk():
    # path = '../../x_disk_system_link/'   # This works in this file localy
    path = 'x_disk_system_link/'
    projects = os.listdir(path=path)

    def get_projects(self):
        return self.projects


# print(OLV_P_Projects_On_Disk().get_projects())