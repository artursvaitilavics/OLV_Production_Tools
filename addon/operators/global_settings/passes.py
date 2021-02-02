import bpy

from .passes_to_nodes import OLV_OP_Passes_To_Nodes
from ..create_comp_nodes import CreateCompNodes
# from .apply_passes import OLV_OP_Apply_Passes


class OLV_OP_Passes(bpy.types.Operator):
    bl_idname = 'olv.passes'
    bl_label = 'Render Passes'

    # passes_to_nodes = OLV_OP_Passes_To_Nodes()
    # apply_passes = OLV_OP_Apply_Passes()

    layer_name = ''

    create_comp_nodes = CreateCompNodes()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        layer_name = bpy.context.window.view_layer.name
        self.apply_passes_globaly(layer_name)

        return{'FINISHED'}


# TODO: Refactor below code, to take all this crap from another module, to keep this one clean.
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

    prop_crypto_accurate: bool_prop(
        name='Cryptomatte Accurate Mode', default=True)

    prop_crypto_levels: int_prop(name='Cryptomatte Levels', default=6)

    # prop_group = [
    #     # prop_combined,
    #     prop_z,
    #     prop_mist,
    #     prop_normal,
    #     prop_vector,
    #     prop_uv,

    #     # TODO make separate, so that denoising node can be created and connected to all inputs, outpts
    #     prop_denoising_data,

    #     prop_diffuse_direct,
    #     prop_diffuse_indirect,
    #     prop_diffuse_color,

    #     prop_glossy_direct,
    #     prop_glossy_indirect,
    #     prop_glossy_color,

    #     prop_transmission_direct,
    #     prop_transmission_indirect,
    #     prop_transmission_color,

    #     prop_volume_direct,
    #     prop_volume_indirect,
    #     prop_emission,
    #     prop_env,
    #     prop_shadow,
    #     prop_ao,
    #     prop_crypto_object,
    #     prop_crypto_material,
    #     prop_crypto_asset,

    # ]

    def apply_passes_globaly(self, layer_name):

        prop_group = {
            'combined': self.prop_combined,

            'z': self.prop_z,
            'mist': self.prop_mist,
            'normal': self.prop_normal,
            'vector': self.prop_vector,
            'uv': self.prop_uv,

            # TODO make separate, so that denoising node can be created and connected to all inputs, outpts
            'denoise_data': self.prop_denoising_data,

            'diff_dir': self.prop_diffuse_direct,
            'dif_indir': self.prop_diffuse_indirect,
            'dif_col': self.prop_diffuse_color,

            # self.prop_glossy_direct,
            # self.prop_glossy_indirect,
            # self.prop_glossy_color,

            # self.prop_transmission_direct,
            # self.prop_transmission_indirect,
            # self.prop_transmission_color,

            # self.prop_volume_direct,
            # self.prop_volume_indirect,
            # self.prop_emission,
            # self.prop_env,
            # self.prop_shadow,
            # self.prop_ao,
            # self.prop_crypto_object,
            # self.prop_crypto_material,
            # self.prop_crypto_asset,

        }

        # scenes = bpy.data.scenes

        for scene in bpy.data.scenes:

            for prop in prop_group:
                if prop_group.get(prop):
                    self.create_comp_nodes.create_slots(
                        scene, layer_name, prop)
                    print('Prop: ', prop)

            try:
                # print("SCENE NAME: ", scene.name) sheit tiks izsauktas metodes no create_com_nodes, jo buus scena name

                self.create_comp_nodes.create_layer_node(
                scene, layer_name)


                # output_node = scene.node_tree.nodes['Output Node']

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

            except Exception as e:
                print(e)
