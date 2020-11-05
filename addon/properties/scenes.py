from .scene import OLV_Scene


class OLV_Scenes():
    bl_idname = 'olv.scenes'

    scene_01 = OLV_Scene('NYC_L', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [14400, 1620], 900, 30, False)
    scene_02 = OLV_Scene('NYC_R', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [14400, 1620], 900, 30, False)
    scene_03 = OLV_Scene('NYC_T', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [2880, 6480], 900, 30, False)
    scene_04 = OLV_Scene('NYC_5x4_L', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [4800, 2160], 900, 30, False)
    scene_05 = OLV_Scene('NYC_4x4_TH', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [3840, 2160], 900, 30, False)
    scene_06 = OLV_Scene('SYD_4x4', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [3840, 2160], 900, 30, False)
    scene_07 = OLV_Scene('SYD_R', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [11520, 1080], 900, 30, False)
    scene_08 = OLV_Scene('SYD_T', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [2880, 5940], 900, 30, False)
    scene_09 = OLV_Scene('SYD_XG_1L', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [3840, 1080], 900, 30, False)
    scene_10 = OLV_Scene('SYD_XG_2L', 'CYCLES', 'GPU', 512, 16,
                         True, 'Standard', [5760, 1080], 900, 30, False)
    scene_11 = OLV_Scene('LON_Above_Stairs', 'CYCLES', 'GPU',
                         512, 16, True, 'Standard', [3840, 1620], 900, 30, False)
    scene_12 = OLV_Scene('LON_Column_1', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [960, 2970], 900, 30, False)
    scene_13 = OLV_Scene('LON_Column_2', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [960, 2970], 900, 30, False)
    scene_14 = OLV_Scene('LON_Directory', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [3360, 2160], 900, 30, False)
    scene_15 = OLV_Scene('LON_Mixed_Reality', 'CYCLES', 'GPU',
                         512, 16, True, 'Standard', [1440, 1080], 900, 30, False)
    scene_16 = OLV_Scene('LON_Ride_Long', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [5760, 1080], 900, 30, False)
    scene_17 = OLV_Scene('LON_Ride_Short', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [3840, 1080], 900, 30, False)
    scene_18 = OLV_Scene('LON_Runway', 'CYCLES', 'GPU', 512,
                         16, True, 'Standard', [9600, 2610], 900, 30, False)

    ms_project_scenes = [scene_01, scene_02, scene_03, scene_04, scene_05, scene_06, scene_07, scene_08,
                         scene_09, scene_10, scene_11, scene_12, scene_13, scene_14, scene_15, scene_16, scene_17, scene_18]

    def get_scenes(self):
        return self.ms_project_scenes
