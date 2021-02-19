import bpy
from .passes_settings import PassesSettings


class ActiveRenderPasses:
    layer_passes = PassesSettings().get_all_passes()

    def set_passes(self, view_layer):
        layer_passes = self.layer_passes

        layer_passes['Image'] = view_layer.use_pass_combined

        layer_passes['Depth'] = view_layer.use_pass_z
        layer_passes['Mist'] = view_layer.use_pass_mist
        layer_passes['Normal'] = view_layer.use_pass_normal
        layer_passes['Vector'] = view_layer.use_pass_vector
        layer_passes['UV'] = view_layer.use_pass_uv

        layer_passes['Denoise'] = view_layer.cycles.denoising_store_passes

        layer_passes['DiffDir'] = view_layer.use_pass_diffuse_direct
        layer_passes['DiffInd'] = view_layer.use_pass_diffuse_indirect
        layer_passes['DiffCol'] = view_layer.use_pass_diffuse_color

        layer_passes['GlossDir'] = view_layer.use_pass_glossy_direct
        layer_passes['GlossInd'] = view_layer.use_pass_glossy_indirect
        layer_passes['GlossCol'] = view_layer.use_pass_glossy_color

        layer_passes['TransDir'] = view_layer.use_pass_transmission_direct
        layer_passes['TransInd'] = view_layer.use_pass_transmission_indirect
        layer_passes['TransCol'] = view_layer.use_pass_transmission_color

        layer_passes['VolumeDir'] = view_layer.cycles.use_pass_volume_direct
        layer_passes['VolumeInd'] = view_layer.cycles.use_pass_volume_indirect

        layer_passes['Emit'] = view_layer.use_pass_emit
        layer_passes['Env'] = view_layer.use_pass_environment
        layer_passes['Shadow'] = view_layer.use_pass_shadow
        layer_passes['AO'] = view_layer.use_pass_ambient_occlusion

        return self.layer_passes
