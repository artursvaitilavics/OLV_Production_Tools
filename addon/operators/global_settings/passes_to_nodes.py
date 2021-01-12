import bpy

class OLV_OP_Passes_To_Nodes(bpy.types.Operator):
    bl_idname = 'olv.passes_to_nodes'
    bl_label = 'Create output nodes from enabled passes'


    def execute(self):
        print('DEBUGING - passe to nodes execute is called!')