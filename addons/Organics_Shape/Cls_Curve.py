import bpy
import sys
import os
from . import juju
from . import GeoNode


### CURVES CLASS BEGIN ###

class CURVE_curve_to_tube(bpy.types.Operator):
    bl_idname = "object.curve_to_tube"
    bl_label = "curve to tube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.curve_to_tube()
        return {'FINISHED'}

### CURVES CLASS END ###


def register():
    bpy.utils.register_class(CURVE_curve_to_tube)

def unregister():
    bpy.utils.unregister_class(CURVE_curve_to_tube)

