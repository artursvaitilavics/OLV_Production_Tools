import bpy


class OLV_OP_Render_Samples(bpy.types.Operator):
    bl_idname = 'olv.render_samples'
    bl_label = 'Render Samples'

    samples = bpy.props.IntProperty(name='Samples: ', default=512)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        for scene in bpy.data.scenes:
            scene.cycles.samples = self.samples
        return {'FINISHED'}


# TODO: Refresh Sampling window in properties
