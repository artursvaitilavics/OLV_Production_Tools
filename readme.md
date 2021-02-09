OLV Production Tools



For new Network, "settings.jsone" must be updated


################################ Installation ###################################

################################# admin ######################################
change dirrectories for "Xdrive path" and "Assets Path" in settings.json which
is in main folder


from: 

{
    "Xdrive path": "/home/artursvaitilavics/test_paths/test_x_disk/",
    "Assets path": "/home/artursvaitilavics/test_paths/test_assets/",
    "Render Path": "//../../02_Assets/02_3D/"
}


to:

{
    "Xdrive path": "X:\\SSDstorage\\",
    "Assets path": "X:\\Transfer\\ArtursV\\Assets\\"
    "Render Path": "//../../02_Assets/02_3D/"
}
#################################### user ################################################


cmd -> run as Administrator ->
-> paste this command ->

mklink /D "C:\Program Files\Blender Foundation\Blender 2.90\2.90\scripts\addons\OLV_Production_Tools" "X:\Transfer\ArtursV\addons\OLV_Production_Tools"

-> open blender -> enable OLV Tools Plugin -> enjoye Errors


######################################################################



1. Create directory in OLV_Tools called: assets_system_link
2. Pace LON_DepthBox.blend in this directory
3. Create directory in OLV_Tools called: x_disk_system_link

Place this plugin in your BlenderRender/scripts/addons/ directory


suggestion, use SymLink fo