import bpy

from .main_menu import OLV_MT_Main_Menu
from .name_new_project_menu import OLV_MT_Name_New_Project_Menu
from .global_settings_menu import OLV_MT_Global_Settings_Menu
from .object_menu import OLV_MT_Object_Menu

classes = {
    OLV_MT_Main_Menu,
    OLV_MT_Name_New_Project_Menu,
    OLV_MT_Global_Settings_Menu,
    OLV_MT_Object_Menu,

}


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
