import bpy

from .create_new_project import OLV_OP_Create_New_Project
from .create_project_file import OLV_OP_Create_Project_File
from .render_res_percentage import OLV_OP_Set_Resolution_Percentage
from .render_samples import OLV_OP_Render_Samples
from .link_object_to_all_scenes import OLV_OP_Link_Object_To_All_Scenes
from .save_project_file import OLV_OP_Save_Project_File
from .global_settings.passes import OLV_OP_Passes
from .global_settings.view_layers import OLV_OP_View_Layers
from .global_settings.layer_material_overrides import OLV_OP_Layer_Material_Overrides
from .object.bulk_rename import OLV_OP_Bulk_Rename
from .object.bulk_suffix import OLV_OP_Bulk_Suffix
from .object.bulk_prefix import OLV_OP_Bulk_Prefix
from .global_settings.set_world import  OLV_OP_Set_World

# from .global_settings.material_sample_override import OLV_OP_Material_Sample_Overrides
# from .global_settings.passes_to_nodes import OLV_OP_Passes_To_Nodes
# from .project_building.comporitor_output_nodes import OLV_OP_Create_Output_Nodes


classes = (
    OLV_OP_Create_New_Project,
    OLV_OP_Create_Project_File,
    OLV_OP_Set_Resolution_Percentage,
    OLV_OP_Render_Samples,
    OLV_OP_Link_Object_To_All_Scenes,
    OLV_OP_Save_Project_File,
    OLV_OP_Passes,
    OLV_OP_View_Layers,
    OLV_OP_Layer_Material_Overrides,
    OLV_OP_Bulk_Rename,
    OLV_OP_Bulk_Suffix,
    OLV_OP_Bulk_Prefix,
    OLV_OP_Set_World

    # OLV_OP_Material_Sample_Overrides
    # OLV_OP_Passes_To_Nodes
    # OLV_OP_Create_Output_Nodes
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
