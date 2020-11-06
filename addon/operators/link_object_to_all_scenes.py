import bpy


class OLV_OP_Link_Object_To_All_Scenes(bpy.types.Operator):
    bl_idname = 'olv.link_object_to_all_scenes'
    bl_label = 'Link object to all scenes'

    def execute(self, context):
        self.link_to_all_scenes()
        return {'FINISHED'}

    def link_to_all_scenes(self):
        selection = bpy.context.active_object
        for scene in bpy.data.scenes:
            if scene.name != bpy.context.scene.name:
                bpy.ops.object.make_links_scene(scene=scene.name)
