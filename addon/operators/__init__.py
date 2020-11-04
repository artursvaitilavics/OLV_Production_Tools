import bpy

from .create_new_project import OLV_OP_Create_New_Project

classes = (
    OLV_OP_Create_New_Project,
)

def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)