import bpy
from ...properties.materials import OLV_Materials


class OLV_MT_Materials_Menu(bpy.types.Menu):
    bl_idname = 'olv.mt_materials_menu'
    bl_label = 'Project List'
    materials = OLV_Materials()

    def draw(self, context):

        layout = self.layout

        materials = self.materials.get_materials()

        for material in materials:
            lo = layout.operator(
                'olv.op_layer_material_overrides', text=material, icon='MATERIAL')
            lo.material_name = material
