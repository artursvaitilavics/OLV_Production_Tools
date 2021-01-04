import bpy

from ....properties.passes import OLV_P_Passes


class OLV_MT_View_Layer_Sub_Passes(bpy.types.Menu):
    bl_idname = 'olv.view_layer_sub_passes_menu'
    bl_label = 'Sub Passes'

    passes = OLV_P_Passes()

    def draw(self, context):
        layout = self.layout
        keys = self.passes.get_view_layer_passes().keys()
        for key in keys:
            layout.operator('olv.passes', text=key)


class OLV_MT_Data_Sub_Passes(bpy.types.Menu):
    bl_idname = 'olv.view_data_sub_passes_menu'
    bl_label = 'Sub Passes'

    passes = OLV_P_Passes()

    def draw(self, context):
        keys = self.passes.get_passes_data().keys()
        layout = self.layout
        scene = context.scene
        for key in keys:
            
            layout.label(text=key)
            row = layout.row()
            row.prop('passes_value', text='SOME ARTURS TEXT')