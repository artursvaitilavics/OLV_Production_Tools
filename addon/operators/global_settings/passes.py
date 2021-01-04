import bpy


class OLV_OP_Passes(bpy.types.Operator):
    bl_idname = 'olv.passes'
    bl_label = 'Render Passes'

    passes_names = bpy.props.StringProperty('Pass_AV')
    passes_value = bpy.props.BoolProperty(name='passes_value', default=False)

    def execute(self, context):
        print("Pass button presses.")
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
