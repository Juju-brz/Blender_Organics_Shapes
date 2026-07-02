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
from . import Cls_jujuNodes
from . import Cls_Curve
from . import Cls_Volume

def register():
    main.register()
    #panels.register()
    Cls_jujuNodes.register()
    Cls_Curve.register()
    Cls_Volume.register()


def unregister():
    main.unregister()
    #panels.unregister()
    Cls_jujuNodes.unregister()
    Cls_Curve.unregister()
    Cls_Volume.register()



###
#Julien Brouzes juju
