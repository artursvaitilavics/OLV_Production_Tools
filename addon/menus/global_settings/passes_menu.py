import bpy


from ...properties.passes import OLV_P_Passes


class OLV_MT_Passes(bpy.types.Menu):
    bl_idname = 'olv.passes_menu'
    bl_label = 'Passes'

    passes = OLV_P_Passes()
    h1_passes = passes.get_passes()
    h2_passes = passes.get_view_layer_passes()

    def draw(self, context):
        layout = self.layout

        # keys = self.h1_passes.keys()
        keys =  list(self.passes.get_passes().keys())

        layout.menu('olv.view_layer_sub_passes_menu', text=keys[0])

        layout.menu('olv.view_data_sub_passes_menu', text=keys[1])
        # for key in keys:
        #     layout.menu('olv.view_layer_sub_passes_menu', text=key)

