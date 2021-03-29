bl_info = {
    'name' : 'OlvTools',
    'description': 'Olv tools for speeding up mondane tasks.',
    'author': 'Olv Team',
    'version': (1, 0),
    'blender': (2, 90, 1),
    'location': 'View3D',
    'category': '3D View'
    # 'location': 'Compositing',
    # 'category': 'Compositing',
}

def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from .addon.register import unregister_addon
    unregister_addon()