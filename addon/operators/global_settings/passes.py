import bpy


class OLV_OP_Passes(bpy.types.Operator):
    bl_idname = 'olv.passes'
    bl_label = 'Render Passes'

    passses = {
        'View Layer': {
            'use': True,
            'use_single_layer': False,
        },
        'Passes': {
            'use_pass_combined': True,
            'use_pass_z': False,
            'use_pass_mist': False,
            'use_pass_normal': False,
            'use_pass_vector': False,
            'use_pass_uv': False,
            'denoising_store_passes': True,
            'use_pass_object_index': False,
            'use_pass_material_index': False,
            'pass_debug_render_time': False,
            'pass_debug_sample_count': False,
            'pass_alpha_threshold': 0.5
        },
        'Lights': {
            'Diffuse': {
                'use_pass_diffuse_direct': False,
                'use_pass_diffuse_indirect': False,
                'use_pass_diffuse_color': False,
            },
            'Glossy': {
                'use_pass_glossy_direct': False,
                'use_pass_glossy_indirect': False,
                'use_pass_glossy_color': False,
            },
            'Transmission': {
                'use_pass_transmission_direct': False,
                'use_pass_transmission_indirect': False,
                'use_pass_transmission_color': False,
            },
            'Volume': {
                'use_pass_volume_direct': False,
                'use_pass_volume_indirect': False,
            },
            'Other': {
                'use_pass_emit': False,
                'use_pass_environment': False,
                'use_pass_shadow': False,
                'use_pass_ambient_occlusion': False,
            }
        },
        'Cryptomattes': {
            'Iclude': {
                'use_pass_crypto_object': False,
                'use_pass_crypto_material': False,
                'use_pass_crypto_asset': False,
                'pass_crypto_depth': 6,
                'pass_crypto_accurate': False,
            }
        }}
    
    passes_names = bpy.props.StringProperty('Pass_AV')

    def execute(self, context):
        # for scene in bpy.data.scenes:
        #     self.passses.get("Passes")
        return{'FINISHED'}

    # bpy.context.scene.view_layers["img"].use_pass_combined = True - Example

    #  - bellow ones seems differenct from others, as it wont say viewlayer:

    # bpy.context.scene.render.use_single_layer = False
    # bpy.context.scene.denoising_store_passes = True
    # bpy.context.scene.pass_debug_render_time = False
    # bpy.context.scene.pass_debug_sample_count = False
    # bpy.context.scene.use_pass_volume_direct = True
    # bpy.context.scene.use_pass_volume_indirect = True
    # bpy.context.scene.use_pass_crypto_object = True
    # bpy.context.scene.use_pass_crypto_material = True
    # bpy.context.scene.use_pass_crypto_asset = True
    # bpy.context.scene.pass_crypto_depth = 4
    # bpy.context.scene.pass_crypto_accurate = True
