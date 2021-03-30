import bpy

from .main_menu import OLV_MT_Main_Menu
from .name_new_project_menu import OLV_MT_Name_New_Project_Menu
from .global_settings_menu import OLV_MT_Global_Settings_Menu
from .object_menu import OLV_MT_Object_Menu
from .project_list_menu import OLV_MT_Project_List_Menu
from .global_settings.passes_menu import OLV_MT_Passes
from .global_settings.passes_submenus.pases_submenus import OLV_MT_View_Layer_Sub_Passes, OLV_MT_Data_Sub_Passes
from .global_settings.materials_menu import OLV_MT_Materials_Menu


classes = {
    OLV_MT_Main_Menu,
    OLV_MT_Name_New_Project_Menu,
    OLV_MT_Global_Settings_Menu,
    OLV_MT_Object_Menu,
    OLV_MT_Project_List_Menu,
    OLV_MT_Passes,
    OLV_MT_View_Layer_Sub_Passes,
    OLV_MT_Data_Sub_Passes,
    OLV_MT_Materials_Menu
    

}


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
