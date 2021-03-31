import bpy

class OLV_Slot_Name():
    
    def generate_slot(self):
        # Base Path
        relative_path_start = '//../../Assets/3D/'
        blend_file_name = ''
        scene_name = ''

        # Slot Name
        layer_name = ''
        pass_name = ''

        for scene in bpy.data.scenes:
            scene_name = scene.name
            for layer in scene.view_layers:
                layer_name = layer.name
                

  
  
  
  
  
  
        # 3DRenders => blend file name => Scene => Layer => Pass
