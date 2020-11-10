
class OLV_P_Passes():

    passses = {
        'View Layer': {
            'use': True,
            'use_single_layer': False,
        },
        'Passes Data': {
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

            'use_pass_crypto_object': False,
            'use_pass_crypto_material': False,
            'use_pass_crypto_asset': False,
            'pass_crypto_depth': 6,
            'pass_crypto_accurate': False,

        }}

    def get_passes(self):
        return self.passses

    def get_view_layer_passes(self):
        return self.passses.get('View Layer')

    def get_passes_data(self):
        return self.passses.get('Passes Data')

    def get_passes_lights(self):
        return self.passses.get('Lights')

    def get_passes_cryptomattes(self):
        return self.passses.get('Cryptomattes')

# Lights Passes sub passes:

    def get_diffuse(self):
        return self.get_passes_lights().get('Diffuse')

    def get_glossy(self):
        return self.get_passes_lights().get('Glossy')

    def get_transmission(self):
        return self.get_passes_lights().get('Transmission')

    def get_volume(self):
        return self.get_passes_lights().get('Volume')

    def get_other(self):
        return self.get_passes_lights().get('Other')
