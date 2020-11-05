class OLV_Scene():
    bl_idname = 'olv.scene'

    def __init__(self,
                 name,
                 render_engine,
                 render_device,
                 render_samples,
                 viewport_samples,
                 film_transparnecy,
                 color_management_transform,
                 resolution: [],
                 end_frame,
                 frame_rate,
                 z_pass,
                 ):
        self.name = name
        self.render_engine = render_engine
        self.render_device = render_device
        self.render_samples = render_samples
        self.viewport_samples = viewport_samples
        self.film_transparnecy = film_transparnecy
        self.color_management_transform = color_management_transform
        self.resolution = resolution
        self.end_frame = end_frame
        self.frame_rate = frame_rate
        self.z_pass = z_pass
