import bpy
import sys
import os
from . import juju
from . import GeoNode


class NODE_OT_symmetry(bpy.types.Operator):
    bl_idname = "object.symmetry"
    bl_label = "symmetry"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.symmetry_1_node_group(node_tree_names)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(NODE_OT_symmetry)

def unregister():
    bpy.utils.unregister_class(NODE_OT_symmetry)
