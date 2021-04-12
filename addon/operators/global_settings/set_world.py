import bpy


class OLV_OP_Set_World(bpy.types.Operator):

    bl_idname = "olv.op_set_world"
    bl_label = "set current world for all scenes"

    def execute(self, context):
        world = bpy.context.scene.world

        for scene in bpy.data.scenes:
            scene.world = world
        return{'FINISHED'}