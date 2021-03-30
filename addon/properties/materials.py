import bpy


class OLV_Materials():

    def get_materials(self):
        materials = []
        for mat in bpy.data.materials:
            materials.append(mat.name)
        return materials
