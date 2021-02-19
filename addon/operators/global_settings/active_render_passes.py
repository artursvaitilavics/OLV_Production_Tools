import bpy


class LayerPasses:
    passes = {"Image": True}


class ActiveRenderPasses:

    scene = {"layers": []}
    # view_layers = {"layers": []}

    # scenes = bpy.data.scenes

    # view_layer_names = []

    def view_layer(self):
        for layer in self.view_layers():
            print(layer.name)
    #     layer_passes = LayerPasses()

    #     view_layer = {"name": "", "passes": []}
    #     view_layer["name"] = name
    #     view_layer["passes"] = layer_passes.passes

    #     view_layers["layers"].append(view_layer)

    # scene["layers"].append(view_layers)

    def view_layers(self):
        view_layers = []
        for scene in bpy.data.scenes:
            view_layers = scene.view_layers
            self.scene["layers"].append(view_layers)
        return self.scene

#    for view_layer in scene.view_layers:

#         layer_passes['Image'] = view_layer.use_pass_combined
        # scene.view_layers[layer_name].use_pass_z = self.prop_z
        # scene.view_layers[layer_name].use_pass_mist = self.prop_mist
        # scene.view_layers[layer_name].use_pass_normal = self.prop_normal
        # scene.view_layers[layer_name].use_pass_vector = self.prop_vector
        # scene.view_layers[layer_name].use_pass_uv = self.prop_uv
        # scene.view_layers[layer_name].cycles.denoising_store_passes = self.prop_denoising_data

        # scene.view_layers[layer_name].use_pass_object_index = self.prop_object_index
        # scene.view_layers[layer_name].use_pass_material_index = self.prop_material_index

        # scene.view_layers[layer_name].cycles.pass_debug_render_time = self.prop_render_time
        # scene.view_layers[layer_name].cycles.pass_debug_sample_count = self.prop_sample_count

        # scene.view_layers[layer_name].pass_alpha_threshold = self.prop_alpha_threshold

        # scene.view_layers[layer_name].use_pass_diffuse_direct = self.prop_diffuse_direct
        # scene.view_layers[layer_name].use_pass_diffuse_indirect = self.prop_diffuse_indirect
        # scene.view_layers[layer_name].use_pass_diffuse_color = self.prop_diffuse_color

        # scene.view_layers[layer_name].use_pass_glossy_direct = self.prop_glossy_direct
        # scene.view_layers[layer_name].use_pass_glossy_indirect = self.prop_glossy_indirect
        # scene.view_layers[layer_name].use_pass_glossy_color = self.prop_glossy_color

        # scene.view_layers[layer_name].use_pass_transmission_direct = self.prop_transmission_direct
        # scene.view_layers[layer_name].use_pass_transmission_indirect = self.prop_transmission_indirect
        # scene.view_layers[layer_name].use_pass_transmission_color = self.prop_transmission_color

        # scene.view_layers[layer_name].cycles.use_pass_volume_direct = self.prop_volume_direct
        # scene.view_layers[layer_name].cycles.use_pass_volume_indirect = self.prop_volume_indirect

        # scene.view_layers[layer_name].use_pass_emit = self.prop_emission
        # scene.view_layers[layer_name].use_pass_environment = self.prop_env
        # scene.view_layers[layer_name].use_pass_shadow = self.prop_shadow
        # scene.view_layers[layer_name].use_pass_ambient_occlusion = self.prop_ao

        # scene.view_layers[layer_name].cycles.use_pass_crypto_object = self.prop_crypto_object
        # scene.view_layers[layer_name].cycles.use_pass_crypto_material = self.prop_crypto_material
        # scene.view_layers[layer_name].cycles.use_pass_crypto_asset = self.prop_crypto_asset
        # scene.view_layers[layer_name].cycles.pass_crypto_depth = self.prop_crypto_levels
        # scene.view_layers[layer_name].cycles.pass_crypto_accurate = self.prop_crypto_accurate

    # return layer_passes
