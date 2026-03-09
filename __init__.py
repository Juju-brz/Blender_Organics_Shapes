#juju

bl_info = {
    "name": "Blender Organics Shape",
    "blender": (5, 0, 1),
    "category": "Object",
    "version": (0, 1, 2, 0)
}

import bpy
from . import main


def register():
    main.register()
    #panels.register()

def unregister():
    main.unregister()
    #panels.unregister()


###
#Julien Brouzes juju
