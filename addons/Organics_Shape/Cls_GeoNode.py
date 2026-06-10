import bpy
import sys
import os
from . import juju
from . import GeoNode


### NODES  CLASS BEGIN ###

class NODE_OT_symmetry(bpy.types.Operator):
    bl_idname = "object.symmetry"
    bl_label = "symmetry"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.symmetry_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_create_trunk(bpy.types.Operator):
    bl_idname = "object.create_trunk"
    bl_label = "create_trunk"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_trunk_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_volume_simulation(bpy.types.Operator):
    bl_idname = "object.volume_simulation"
    bl_label = "volume_simulation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.volume_simulation(node_tree_names)
        return {'FINISHED'}

class NODE_OT_sprinkle(bpy.types.Operator):
    bl_idname = "object.sprinkle"
    bl_label = "sprinkle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.sprinkle_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_Grid_Volume(bpy.types.Operator):
    bl_idname = "object.grid_volume"
    bl_label = "grid_volume"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.grid_volume_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_Get_Normalize(bpy.types.Operator):
    bl_idname = "object.get_normalize"
    bl_label = "get normalize"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.getnormalize_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_delete_points_of_curve(bpy.types.Operator):
    bl_idname = "object.delete_points_of_curve"
    bl_label = "delete points of curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.delete_points_of_curve_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_create_leafs(bpy.types.Operator):
    bl_idname = "object.create_leafs"
    bl_label = "create leafs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_leafs_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_branches(bpy.types.Operator):
    bl_idname = "object.branches"
    bl_label = "create branches"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_branches_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_thickness(bpy.types.Operator):
    bl_idname = "object.thickness"
    bl_label = "thickness"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.thickness_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_seeds_of_plants(bpy.types.Operator):
    bl_idname = "object.seeds_of_plants"
    bl_label = "seeds of plants"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.seeds_of_plants_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_noise(bpy.types.Operator):
    bl_idname = "object.noise"
    bl_label = "noise"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.noise_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_head(bpy.types.Operator):
    bl_idname = "object.head"
    bl_label = "head"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.head_1_node_group(node_tree_names)
        return {'FINISHED'}

### NODES  CLASS END ###

def register():
    bpy.utils.register_class(NODE_OT_symmetry)
    bpy.utils.register_class(NODE_OT_create_trunk)
    bpy.utils.register_class(NODE_OT_volume_simulation)
    bpy.utils.register_class(NODE_OT_sprinkle)
    bpy.utils.register_class(NODE_OT_Grid_Volume)
    bpy.utils.register_class(NODE_OT_Get_Normalize)
    bpy.utils.register_class(NODE_OT_delete_points_of_curve)
    bpy.utils.register_class(NODE_OT_create_leafs)
    bpy.utils.register_class(NODE_OT_branches)
    bpy.utils.register_class(NODE_OT_thickness)
    bpy.utils.register_class(NODE_OT_seeds_of_plants)
    bpy.utils.register_class(NODE_OT_noise)
    bpy.utils.register_class(NODE_OT_head)

def unregister():
    bpy.utils.unregister_class(NODE_OT_symmetry)
    bpy.utils.unregister_class(NODE_OT_create_trunk)
    bpy.utils.unregister_class(NODE_OT_volume_simulation)
    bpy.utils.unregister_class(NODE_OT_sprinkle)
    bpy.utils.unregister_class(NODE_OT_Grid_Volume)
    bpy.utils.unregister_class(NODE_OT_Get_Normalize)
    bpy.utils.unregister_class(NODE_OT_delete_points_of_curve)
    bpy.utils.unregister_class(NODE_OT_create_leafs)
    bpy.utils.unregister_class(NODE_OT_branches)
    bpy.utils.unregister_class(NODE_OT_thickness)
    bpy.utils.unregister_class(NODE_OT_seeds_of_plants)
    bpy.utils.unregister_class(NODE_OT_noise)
    bpy.utils.unregister_class(NODE_OT_head)

