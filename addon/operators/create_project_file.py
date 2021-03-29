import bpy
import os
import json

from ..properties.scenes import OLV_Scenes
from ..utility.settings import Settings

from math import radians

from .project_building.comporitor_output_nodes import OLV_OP_Create_Output_Nodes
# TODO: Maybe get this to be done when creating new project


class OLV_OP_Create_Project_File(bpy.types.Operator):

    bl_idname = 'olv.create_project_file'
    bl_label = 'Create Project File'

    scenes = OLV_Scenes()
    nodes = OLV_OP_Create_Output_Nodes()

    settings = Settings()

    project_created = False

    # project_exist_message: bpy.props.StringProperty(name = "Project Exists" ,)

    def execute(self, context):

        if not OLV_OP_Create_Project_File.project_created:

            self.import_LON_depth_boxes()
            self.create_scenes()
            self.delete_default_scene()
            self.apply_settings()
            self.nodes.execute()
            OLV_OP_Create_Project_File.project_created = True
        else:
            self.report({"WARNING"}, "Project file already exists...")
            return{"CANCELLED"}

        return {'FINISHED'}

    def create_scenes(self):
        for scene in self.scenes.get_scenes():
            this_scene = bpy.data.scenes.new(scene.name)
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
            scene_blender.view_layers['img'].cycles.denoising_store_passes = scene.denoising_data

    def create_camera(self, scene_name: str):
        scene_name = scene_name + '_Camera'
        camera = bpy.data.cameras.new('Camera')
        camera_object = bpy.data.objects.new(scene_name, camera)
        camera_object.rotation_euler = (radians(90), 0, 0)
        camera_object.location = (0, 0, 0)
        return camera_object

    def import_LON_depth_boxes(self):

        # TODO: Move lond_data info to settings.json
        lond_data = 'LON_DepthBox.blend'

        file_path = self.settings.get_assets_path() + lond_data

        with bpy.data.libraries.load(file_path) as (data_from, data_to):
            data_to.collections = [name for name in data_from.collections]

        return {'FINISHED'}

    def link_depth_box_setup_to_LON(self, scene_name: str):
        db_object = bpy.data.collections[scene_name]
        bpy.data.scenes[scene_name].collection.children.link(
            db_object)
        bpy.data.scenes[scene_name].camera = bpy.data.objects[scene_name + '_Camera']
