import bpy

from bpy.props import BoolProperty

class OLV_Passes_Settings(PropertyGroup):
    my_bool : BoolProperty(
        name='Arturs Bool Propety',
        description='Testing Bool properties from Settings',
        default=False
    )