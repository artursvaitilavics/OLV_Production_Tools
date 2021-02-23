OLV Production Tools



For new Network, "settings.jsone" must be updated



################################# admin ######################################
change dirrectories for "Xdrive path" and "Assets Path" in settings.json which
is in main folder


from: 

{
    "Xdrive path": "/home/artursvaitilavics/test_paths/test_x_disk/",
    "Assets path": "/home/artursvaitilavics/test_paths/test_assets/",
    "Render Path": "//../../02_Assets/02_3D/",
    "Cycles Settings": {

    },
    "Nodes": [
            "CompositorNodeRLayers",
            "CompositorNodeDenoise",
            "CompositorNodeOutputFile"
        ]
}


to:

{
    "Xdrive path": "X:\\SSDstorage\\",
    "Assets path": "X:\\Transfer\\ArtursV\\Assets\\",
    "Render Path": "//../../02_Assets/02_3D/",
    "Cycles Settings": {

    },
    "Nodes": [
            "CompositorNodeRLayers",
            "CompositorNodeDenoise",
            "CompositorNodeOutputFile"
        ]
}


#################################### Installation ################################################

Windows:

windows search -> cmd -> run as Administrator ->
-> paste command:


mklink /D "C:\Program Files\Blender Foundation\Blender 2.90\2.90\scripts\addons\OLV_Production_Tools" "X:\Transfer\ArtursV\addons\OLV_Production_Tools"


IMPORTANT:
------------    make sure "Blender 2.90\2.90" is same version as installed on your PC  -----------------------


-> open blender -> Preferences -> addons -> enable OLV Tools Plugin -> now you can acces olv plugins by having your mouse over 3D Viewport and press:
CTRL+SHIFT+X
-> TEST IT -> send feedback, errors and additional update suggestions



###################################################################### Description #################################################################
to acces tools:
CTRL+SHIFT+X

Project:
    Set Project File - Creates new MS project file.
    New Project - Creates project folder structure on Xdrive
    Save File - renames current file to selected project name, and saves it in appropriate project folder -> production -> 3D

Global Settings:
    Resolution Percentage - Sets resolution to all scens in .blend file
    Render Samples - Sets samples for all scenes in .blend file
    Passes - Sets choses render passes to all view layers with the same name across all scenes, 
                Also creates all necessary compositin nodes, RenderLayer, FileOutput and Denoise nodes.
            WARNING: Will delete any compositing nodes, that are currently created. 
            ERRORS: Little issue with Denoise node, it sometimes won't connect to File Output node.
    New View Layer - Creates new view layer across all scenes. (please dont use _ in name of layer, "NewLayerName" this convention is better, at the moment!)

Objects:
    Link to all scenes - links all selected object to all scenes. But only if selected in view port, won't work for Collections