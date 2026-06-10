#juju

bl_info = {
    "name": "Blender Organics Shape",
    "author": "Julien Brouzes",
    "blender": (4, 0, 0),
    "category": "Object",
    "version": (0, 51, 0, 0)
}

import bpy
from . import main
from . import Cls_GeoNode

def register():
    main.register()
    #panels.register()
    Cls_GeoNode.register()


def unregister():
    main.unregister()
    #panels.unregister()
    Cls_GeoNode.unregister()


###
#Julien Brouzes juju
