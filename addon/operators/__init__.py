import bpy

from .create_new_project import OLV_OP_Create_New_Project
from .create_project_file import OLV_OP_Create_Project_File

classes = (
    OLV_OP_Create_New_Project,
    OLV_OP_Create_Project_File
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
