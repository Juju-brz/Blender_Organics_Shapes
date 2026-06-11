import bpy
import sys
import os
from . import juju
from . import GeoNode


class MESH_OT_mesh_to_Volume(bpy.types.Operator):
    bl_idname = "object.mesh_to_volume"
    bl_label = "mesh_to_volume"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.mesh_to_volume()
        return {'FINISHED'}


class MESH_OT_volume_to_Mesh(bpy.types.Operator):
    bl_idname = "object.volume_to_mesh"
    bl_label = "volume_to_mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.volume_to_mesh()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MESH_OT_mesh_to_Volume)
    bpy.utils.register_class(MESH_OT_volume_to_Mesh)

def unregister():
    bpy.utils.unregister_class(MESH_OT_mesh_to_Volume)
    bpy.utils.unregister_class(MESH_OT_volume_to_Mesh)
