def register_addon():

    # from ..properties import register_properties
    # register_properties()
    # from ..operators.project_building import register_project_building
    # register_project_building()

    from ..menus import register_menus
    register_menus()

    from ..operators import register_operators
    register_operators()

    from .keymap import register_keymap
    register_keymap()


def unregister_addon():

    # from ..properties import unregister_properties
    # unregister_properties()
    # from ..operators.project_building import unregister_project_building
    # unregister_project_building()

    from ..menus import unregister_menus
    unregister_menus()

    from ..operators import unregister_operators
    unregister_operators()

    from .keymap import unregister_keymap
    unregister_keymap()
