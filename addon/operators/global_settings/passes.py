import bpy


class OLV_OP_Passes(bpy.types.Operator):
    bl_idname = 'olv.passes'
    bl_label = 'Render Passes'

    layer_name = 'img'

    bool_prop = bpy.props.BoolProperty
    float_prop = bpy.props.FloatProperty
    int_prop = bpy.props.IntProperty

    prop_use_for_rendering: bool_prop(name='Use for rendering', default=True)
    prop_single_layer: bool_prop(name='Render single layer', default=False)

    prop_combined: bool_prop(name='Combined', default=True)
    prop_z: bool_prop(name='Z', default=False)
    prop_mist: bool_prop(name='Mist', default=False)
    prop_normal: bool_prop(name='Normal', default=False)
    prop_vector: bool_prop(name='Vector', default=False)
    prop_uv: bool_prop(name='UV', default=False)
    prop_denoising_data: bool_prop(name='Denoising Data', default=True)
    prop_object_index: bool_prop(name='Object Index', default=False)
    prop_material_index: bool_prop(name='Material Index', default=False)
    prop_render_time: bool_prop(name='Render Time', default=False)
    prop_sample_count: bool_prop(name='Sample Count', default=False)
    prop_alpha_threshold: float_prop(name='Alpha Threshold', default=0.5)

    prop_diffuse_direct: bool_prop(name='Diffuse Direct', default=False)
    prop_diffuse_indirect: bool_prop(name='Diffuse Indirect', default=False)
    prop_diffuse_color: bool_prop(name='Diffuse Color', default=False)
    prop_glossy_direct: bool_prop(name='Glossy Direct', default=False)
    prop_glossy_indirect: bool_prop(name='Glossy Indirect', default=False)
    prop_glossy_color: bool_prop(name='Glossy Color', default=False)
    prop_transmission_direct: bool_prop(
        name='Transmission Direct', default=False)
    prop_transmission_indirect: bool_prop(
        name='Transmission Indirect', default=False)
    prop_transmission_color: bool_prop(
        name='Transmission Color', default=False)
    prop_volume_direct: bool_prop(name='Volume Direct', default=False)
    prop_volume_indirect: bool_prop(name='Volume Indirect', default=False)
    prop_emission: bool_prop(name='Emission', default=False)
    prop_env: bool_prop(name='Environment', default=False)
    prop_shadow: bool_prop(name='Shadow', default=False)
    prop_ao: bool_prop(name='Ambient Oclusion', default=False)

    prop_crypto_object: bool_prop(name='Cryptomatte Object', default=False)
    prop_crypto_material: bool_prop(name='Cryptomatte Material', default=False)
    prop_crypto_asset: bool_prop(name='Cryptomatte Asset', default=False)
    prop_crypto_levels: int_prop(name='Cryptomatte Levels', default=6)
    prop_crypto_accurate: bool_prop(
        name='Cryptomatte Accurate Mode', default=True)
    # prop_: bool_prop(name='', default=False)
    # prop_: bool_prop(name='', default=False)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        layer_name = self.layer_name

        for scene in bpy.data.scenes:
            # TODO: check if looping through all view layers could be useful
            # TODO: extract method for this loop so it's easier to select which view layers have this settings
            # TODO: layer_name could be taken from currently active view layer in context 
            scene.view_layers[layer_name].use = self.prop_use_for_rendering
            scene.render.use_single_layer = self.prop_single_layer

            scene.view_layers[layer_name].use_pass_combined = self.prop_combined
            scene.view_layers[layer_name].use_pass_z = self.prop_z
            scene.view_layers[layer_name].use_pass_mist = self.prop_mist
            scene.view_layers[layer_name].use_pass_normal = self.prop_normal
            scene.view_layers[layer_name].use_pass_vector = self.prop_vector
            scene.view_layers[layer_name].use_pass_uv = self.prop_uv
            scene.view_layers[layer_name].cycles.denoising_store_passes = self.prop_denoising_data

            scene.view_layers[layer_name].use_pass_object_index = self.prop_object_index
            scene.view_layers[layer_name].use_pass_material_index = self.prop_material_index

            scene.view_layers[layer_name].cycles.pass_debug_render_time = self.prop_render_time
            scene.view_layers[layer_name].cycles.pass_debug_sample_count = self.prop_sample_count

            scene.view_layers[layer_name].pass_alpha_threshold = self.prop_alpha_threshold

            scene.view_layers[layer_name].use_pass_diffuse_direct = self.prop_diffuse_direct
            scene.view_layers[layer_name].use_pass_diffuse_indirect = self.prop_diffuse_indirect
            scene.view_layers[layer_name].use_pass_diffuse_color = self.prop_diffuse_color

            scene.view_layers[layer_name].use_pass_glossy_direct = self.prop_glossy_direct
            scene.view_layers[layer_name].use_pass_glossy_indirect = self.prop_glossy_indirect
            scene.view_layers[layer_name].use_pass_glossy_color = self.prop_glossy_color

            scene.view_layers[layer_name].use_pass_transmission_direct = self.prop_transmission_direct
            scene.view_layers[layer_name].use_pass_transmission_indirect = self.prop_transmission_indirect
            scene.view_layers[layer_name].use_pass_transmission_color = self.prop_transmission_color

            scene.view_layers[layer_name].cycles.use_pass_volume_direct = self.prop_volume_direct
            scene.view_layers[layer_name].cycles.use_pass_volume_indirect = self.prop_volume_indirect

            scene.view_layers[layer_name].use_pass_emit = self.prop_emission
            scene.view_layers[layer_name].use_pass_environment = self.prop_env
            scene.view_layers[layer_name].use_pass_shadow = self.prop_shadow
            scene.view_layers[layer_name].use_pass_ambient_occlusion = self.prop_ao

            scene.view_layers[layer_name].cycles.use_pass_crypto_object = self.prop_crypto_object
            scene.view_layers[layer_name].cycles.use_pass_crypto_material = self.prop_crypto_material
            scene.view_layers[layer_name].cycles.use_pass_crypto_asset = self.prop_crypto_asset
            scene.view_layers[layer_name].cycles.pass_crypto_depth = self.prop_crypto_levels
            scene.view_layers[layer_name].cycles.pass_crypto_accurate = self.prop_crypto_accurate

        return{'FINISHED'}
