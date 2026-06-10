import bpy
import sys
import os
from . import juju
from . import GeoNode


### CURVES CLASS BEGIN ###

class CURVE_draw_curve(bpy.types.Operator):
    bl_idname = "object.draw_curve"
    bl_label = "draw_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.draw_curve()
        return {'FINISHED'}

class CURVE_curve_to_tube(bpy.types.Operator):
    bl_idname = "object.curve_to_tube"
    bl_label = "curve to tube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.curve_to_tube()
        return {'FINISHED'}

class CURVE_subdivid_curve(bpy.types.Operator):
    bl_idname = "object.subdivid_curve"
    bl_label = "subdivid_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.subdivid_curve()
        return {'FINISHED'}

class CURVE_curve_test(bpy.types.Operator):
    bl_idname = "object.curve_test"
    bl_label = "curve_test"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.curve_test()
        return {'FINISHED'}

class CURVE_procedural_curve(bpy.types.Operator):
    bl_idname = "object.procedural_curve"
    bl_label = "procedural_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.procedural_arc_curve()
        return {'FINISHED'}

class CURVE_fib_curve(bpy.types.Operator):
    bl_idname = "object.fib_curve"
    bl_label = "fib_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.fib_curve()
        return {'FINISHED'}

### CURVES CLASS END ###


def register():
    bpy.utils.register_class(CURVE_draw_curve)
    bpy.utils.register_class(CURVE_curve_to_tube)
    bpy.utils.register_class(CURVE_subdivid_curve)
    bpy.utils.register_class(CURVE_curve_test)
    bpy.utils.register_class(CURVE_procedural_curve)
    bpy.utils.register_class(CURVE_fib_curve)

def unregister():
    bpy.utils.unregister_class(CURVE_draw_curve)
    bpy.utils.unregister_class(CURVE_curve_to_tube)
    bpy.utils.unregister_class(CURVE_subdivid_curve)
    bpy.utils.unregister_class(CURVE_curve_test)
    bpy.utils.unregister_class(CURVE_procedural_curve)
    bpy.utils.unregister_class(CURVE_fib_curve)

