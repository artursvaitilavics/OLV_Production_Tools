
4. Make visible for which layers we are creating nodes/ enabling passes.
4.1. Have a matrix menu with checkboxes for Scenes => Layers => Passes. This is so we can chose
    specific scenes and layers, for which we need to enable global passes...

6. Coppy view layers from scene to newly created scenes.

7. Passes should smoothly work also for Eevee

8. Created nodes should be sorted in readably manner




18. Compositing nodes, could update instead of reset
    - list of all nodes and their inputs names and so on.
    - if calling passes not first time, then assign all settigns from above data 
    - and assign newly clicked passes...
    - needs more planning

19. seperate save new project and save increment
21. Production => 3D => master_file and directory with older version.
22. OLV MEnu => Project => Create Assets File
23. Option to see list of all the materials and textures.
24. Proper Material Library, have Material Master file on server. And we can access all those files from Active Blender Scene
    Copy the materilas in to current Blender File, and all necesary textures to the Active Project Assets directory.
25. Renaming tool - Bulk rename, add/remove/edit suffixes/preffexes.
Add otopns:
choose how many zeroes you have when renaming, now it's _1 _2 _3... there should be an option for _01 _02, _001 _002 etc.
When adding sufix add check for numbers, if there're then sufix should be added before numbers, now Sphere.001_FOR_FUN, should be Sphere_FOR_FUN.001, toggle for this option would be nice.
Also if let's say you made a mistake and want to adjust prefix/sufix, you should have replace option, where you type what to look for and what to replace it with.

26. If Mesh has unique material, then it should take the name of the mesh, and add suffix "_mat"
27. OPTIONAL - Renaming of the baked textures on the disk. (idea update comming soon from Marius)
12. OPTIONAL - Temp directory might not be needed.


Kristaps:
    Clear custom transformations:


import bpy


class TRANSFORM_OT_clear_orientations(bpy.types.Operator):
bl_idname = 'transform.clear_orientations'
bl_label = 'Clear Transform Orientations'

def execute(self, context):
    for t in context.scene.orientations:
        context.space_data.transform_orientation = t.name
        override = {
            'context': context,
            'area': context.area,
            'window': context.window,
            'screen': context.screen,
            'scene': context.scene,
            'region': context.region,
            'name': t.name
        }
        bpy.ops.transform.delete_orientation(override)
    return {"FINISHED"}


def register():
bpy.utils.register_class(TRANSFORM_OT_clear_orientations)
hotkey = bpy.context.window_manager.keyconfigs.active.keymaps['3D View'].keymap_items.new
hotkey('transform.clear_orientations', type='T',
        shift=True, ctrl=True, value='PRESS')





or 



for area in bpy.context.screen.areas:
 
 print ('area.type=',area.type)
 
 if area.type == 'VIEW_3D':
  r3d = area.spaces[0].region_3d
 
  # access viewport stuff here, e.g.
  print(r3d.perspective_matrix)
#  bpy.ops.transform.delete_orientation()
#  print ( 'deleted')
 
  for t in bpy.context.scene.orientations:
 
# if  t.name=="
   print (' before  t,name=',t.name  )
   bpy.context.space_data.transform_orientation = t.name
   print ('  here    t,name=',t.name  )
 
   override = {
    'context':context,
    'area':context.area,
    'window':context.window,
    'screen':context.screen,
    'scene':context.scene,
    'region':context.region,
    'name':t.name
    }
   
   bpy.ops.transform.delete_orientation(override)
