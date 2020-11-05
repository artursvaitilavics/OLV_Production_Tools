import bpy
import os

from ..properties.scenes import OLV_Scenes
from math import radians

# TODO: Maybe get this to be done when creating new project


class OLV_OP_Create_Project_File(bpy.types.Operator):

    bl_idname = 'olv.create_project_file'
    bl_label = 'Create Project File'

    scenes = OLV_Scenes()

    # TODO: find a way to get this path quick and simple for artist
    path = 'x_disk_system_link/MS_BTS_FY_2025/03_Production/01_3D/'
    file_name = 'Test_Name_v001.blend'

    # TODO: list all projects on X disk

    def execute(self, context):
        self.import_LON_depth_boxes()
        self.create_scenes()
        self.delete_default_scene()
        self.apply_settings()
        # self.link_depth_box_setup_to_LON()
        # TODO: Uncoment below line, to save project file
        # bpy.ops.wm.save_as_mainfile(filepath=self.path + '/' + self.file_name)
        return {'FINISHED'}

    def create_scenes(self):
        for scene in self.scenes.get_scenes():
            this_scene = bpy.data.scenes.new(scene.name)
            # Could be better than checking for L in the name of the scene
            if scene.name[0] != 'L':
                camera = self.create_camera(scene.name)
                this_scene.collection.objects.link(camera)
                this_scene.camera = camera
            else:
                self.link_depth_box_setup_to_LON(scene.name)

    def delete_default_scene(self):

        bpy.ops.scene.delete()

    def apply_settings(self):
        for scene in self.scenes.get_scenes():
            scene_blender = bpy.data.scenes[scene.name]
            scene_blender.render.engine = scene.render_engine
            scene_blender.cycles.device = scene.render_device
            scene_blender.cycles.samples = scene.render_samples
            scene_blender.cycles.preview_samples = scene.viewport_samples
            scene_blender.render.film_transparent = scene.film_transparnecy
            scene_blender.view_settings.view_transform = scene.color_management_transform
            scene_blender.render.resolution_x = scene.resolution[0]
            scene_blender.render.resolution_y = scene.resolution[1]
            scene_blender.frame_end = scene.end_frame
            scene_blender.render.fps = scene.frame_rate
            scene_blender.view_layers['View Layer'].name = 'img'
            scene_blender.view_layers['img'].use_pass_z = scene.z_pass

    def create_camera(self, scene_name: str):
        scene_name = scene_name + '_Camera'
        camera = bpy.data.cameras.new('Camera')
        camera_object = bpy.data.objects.new(scene_name, camera)
        camera_object.rotation_euler = (radians(90), 0, 0)
        camera_object.location = (0, -5, 1)
        return camera_object

    def import_LON_depth_boxes(self):

        file_path = 'assets_system_link/LON_DepthBox.blend'

        with bpy.data.libraries.load(file_path) as (data_from, data_to):
            data_to.collections = [name for name in data_from.collections]

        return {'FINISHED'}

    def link_depth_box_setup_to_LON(self, scene_name: str):
        db_object = bpy.data.collections[scene_name]
        bpy.data.scenes[scene_name].collection.children.link(
            db_object)
        bpy.data.scenes[scene_name].camera = bpy.data.objects[scene_name + '_Camera']
