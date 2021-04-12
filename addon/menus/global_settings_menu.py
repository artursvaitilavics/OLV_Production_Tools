import bpy

class OLV_MT_Global_Settings_Menu(bpy.types.Menu):
    bl_idname = 'olv.global_settings_menu'
    bl_label = 'Global Settings'

    def draw(self, context):
        layout = self.layout

        layout.operator('olv.set_resolution_percentage', text='Resolution Percentage', icon='VIEW_CAMERA')
        layout.operator('olv.op_set_world', text='World copy to all scenes', icon='WORLD_DATA')
        layout.operator('olv.render_samples', text='Render Samples', icon='SHADERFX')
        layout.operator('olv.passes', text='Passes', icon='RENDERLAYERS')#TODO: Connect or disconnect output nodes
        layout.operator('olv.view_layers', text='New View Layer', icon='RENDERLAYERS')
        # layout.operator('olv.op_layer_material_overrides', text='Material overrides', icon='MATERIAL')
        layout.menu('olv.mt_materials_menu', text='Material overrides', icon='MATERIAL')

        