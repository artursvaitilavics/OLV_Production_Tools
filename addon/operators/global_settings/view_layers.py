import bpy


class OLV_OP_View_Layers(bpy.types.Operator):
    bl_idname = "olv.view_layers"
    bl_label = "View Layers class"

    layer_name = bpy.props.StringProperty(
        name="New layer name: ", default="new_view_layer")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        view_layer = self.__create_new_view_layer()
        bpy.context.window.view_layer = view_layer
        return{"FINISHED"}

    def __create_new_view_layer(self):
        
        for scene in bpy.data.scenes:
            view_layer = scene.view_layers.new(self.layer_name)
        
        return view_layer
        
