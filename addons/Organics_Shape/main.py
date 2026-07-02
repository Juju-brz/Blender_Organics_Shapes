"""
juju Julien BROUZES
https://github.com/Juju-brz
"""

import bpy
import sys
import os
from . import juju
from . import jujuNodes
from . import Cls_jujuNodes
from . import Cls_Curve
from . import Cls_Volume
from . import jujurig

### CLASS BEGIN ###


### VOLUME CLASS BEGIN ###

class MESH_OT_hide_mesh(bpy.types.Operator):
    bl_idname = "object.hide_mesh"
    bl_label = "hide_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #props = context.scene.voxel_terrain_props
        juju.toggle_mesh_visibility()
        return {'FINISHED'}


class NODE_OT_create_geometry_node(bpy.types.Operator):
    bl_idname = "object.create_geometry_node"
    bl_label = "create_geometry_node"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_geometry_node()
        return {'FINISHED'}

class MESH_OT_subdivision_mesh(bpy.types.Operator):
    bl_idname = "object.subdivision_mesh"
    bl_label = "subdivision_mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.subdivision_mesh()
        return {'FINISHED'}

### VOLUME CLASS  END ###


### PLANT GENERATOR  BEGIN ###

class MESH_OT_create_leaf(bpy.types.Operator):
    bl_idname = "object.create_leaf"
    bl_label = "create_leaf"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_leaf(juju.create_leaf_shape)
        return {'FINISHED'}

class MESH_OT_create_spike(bpy.types.Operator):
    bl_idname = "object.create_spike_shape"
    bl_label = "create_spike_shape"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_leaf(juju.create_spike_shape)
        return {'FINISHED'}


### PLANT GENERATOR  END ###


### RIG CLASS BEGIN ###
class RIG_OT_controller_to_points(bpy.types.Operator):
    bl_idname = "object.controller_to_points"
    bl_label = "controller_to_points"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        jujurig.controller_to_points()
        return {'FINISHED'}


### RIG CLASS END ###

### CLASS END  ###

####    UI BEGIN    ####


### 3D PANEL BEGIN ###

# N-Panel to 3D viewport
class VIEW3D_PT_Organics_Generation(bpy.types.Panel):
    bl_label = "ORGANICS GENERATION"
    bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"
    
    def draw(self, context):
        layout = self.layout

        layout.label(text="by juju")
        layout.operator("object.create_geometry_node", text="create_Geometry_node")

class VIEW3D_PT_Volume_Generation(bpy.types.Panel):
    bl_label = "VOLUME"
    bl_idname = "VIEW3D_PT_VolumeGeneration"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Select Mesh")
        layout.operator("object.mesh_to_volume", text="mesh to Volume")
        layout.operator("object.hide_mesh", text="hide / unhide mesh")
        layout.label(text='Select volume')
        layout.operator("object.volume_to_mesh", text="volume to Mesh")
        layout.operator("object.subdivision_mesh", text="Subdivision_mesh")

class VIEW3D_PT_PlantGeneration(bpy.types.Panel):
    bl_label = "PLANT GENERATOR"
    bl_idname = "VIEW3D_PT_PlantGeneration"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"

    def draw(self, context):
        layout = self.layout

        layout.label(text='Create Curve')
        layout.operator("object.draw_curve", text="Draw Curve")
        layout.operator("object.create_leaf", text="Draw leaf")

        layout.separator()
        layout.label(text='modify curve')
        layout.operator("object.create_spike_shape", text="create spike")
        layout.operator("object.subdivid_curve", text="subdivid curve")


### 3D PANEL END ###


### NODE PANEL BEGIN ###

# N-Panel to Geometry Nodes
class NODE_PT_juju_operator(bpy.types.Operator):
    bl_idname = "node.juju_operator"
    bl_label = "juju_operator"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        return {'FINISHED'}


class NODE_PT_Organics_Generation(bpy.types.Panel):
    bl_label = "ORGANICS GENERATION"
    bl_idname = "NODE_PT_Organics_Generation"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.create_geometry_node", text="create geometry node")
        layout.operator("object.symmetry", text="symmetry")


class NODE_PT_Plant_Generator(bpy.types.Panel):
    bl_label = "PLANT GENERATOR"
    bl_idname = "NODE_PT_Plant_Generator"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.label(text='create procedural curve')
        layout.operator("object.procedural_curve", text="Arc Curve")

        layout.label(text='modify curve')
        layout.operator("object.create_trunk", text="Create Trunk")

        layout.operator("object.get_normalize", text="Get Normalize")
        layout.operator("object.delete_points_of_curve", text="delete points of curve")
        layout.operator("object.thickness", text="Thickness")
        layout.operator("object.noise", text="Noise")

        layout.label(text='modify mesh')
        layout.operator("object.sprinkle", text="Spinkle")
        layout.label(text = 'Tree')
        layout.operator("object.seeds_of_plants", text="Seeds of Plants")
        layout.operator("object.branches", text="Create Branches")
        layout.operator("object.create_leafs", text="Create Leafs")
        layout.label(text = 'Plant')
        layout.operator("object.head", text="Head")
        layout.label(text = "test")
        layout.operator("object.hairs", text="Hairs")


class NODE_PT_Volume(bpy.types.Panel):
    bl_label = "VOLUME"
    bl_idname = "NODE_PT_Volume"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.volume_simulation", text="volume simulation")
        layout.operator("object.grid_volume" , text="grid volume")
        layout.operator("object.vert_to_sphere", text="Vertice to Sphere")


### NODE PANEL END ###

### MT_Menu BEGIN ###

# Menu Panel
class ORGANICS_MT_Menu(bpy.types.Menu):
    bl_label = "Organics"
    bl_idname = "ORGANICS_MT_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Organic Tools", icon='PARTICLES')
        layout.separator()
        layout.label(text="truc")
        layout.operator("object.draw_curve", text="Draw Curve")
        layout.operator("object.curve_to_tube", text="Curve to Tube")

        # MENU
        layout.menu("VIEW3D_MT_transform")
        layout.menu("VIEW3D_PT_PlantGeneration")
        layout.operator_menu_enum("object.hide_mesh", "type", text="SubMenu Test")
        layout.separator()
        layout.label(text="RIG")
        layout.label(text="Curve_rig")
        layout.operator("object.controller_to_points", text="controller to points")

        ## EDIT CURVE
        if context.mode == 'EDIT_CURVE':
            layout.label(text="its works !!!")
            layout.operator("object.curve_test", text="curve test")
            layout.operator("object.fib_curve", text="fib curve")
            # Access this operator as a sub-menu.
            layout.operator_menu_enum("object.select_by_type", "type", text="Select All by Type")

        # EDIT MESH
        if context.mode == 'EDIT_MESH':
            layout.label(text="its works !!!")


def draw_menu(self, context):
    self.layout.separator()
    #Call class ORGANICS_MT_Menu
    self.layout.menu("ORGANICS_MT_menu", text="Organics", icon='OUTLINER_OB_POINTCLOUD')

### MT_Menu END ###

####    UI END      ####


### REGISTER BEGIN ###
classes = [
    NODE_PT_juju_operator,
    #NODE_PT_juju_panel,
]

def register():
    ## UI ##
    bpy.utils.register_class(VIEW3D_PT_Organics_Generation)
    bpy.utils.register_class(VIEW3D_PT_Volume_Generation)
    bpy.utils.register_class(VIEW3D_PT_PlantGeneration)
    bpy.utils.register_class(NODE_PT_Organics_Generation)
    bpy.utils.register_class(NODE_PT_Volume)
    bpy.utils.register_class(NODE_PT_Plant_Generator)

    bpy.utils.register_class(ORGANICS_MT_Menu)
    bpy.types.VIEW3D_HT_header.append(draw_menu) # ADD PANEL

    bpy.utils.register_class(NODE_OT_create_geometry_node)

    ## VOLUME ##
    bpy.utils.register_class(MESH_OT_hide_mesh)
    bpy.utils.register_class(MESH_OT_subdivision_mesh)

    ## PLANT ##
    bpy.utils.register_class(MESH_OT_create_leaf)
    bpy.utils.register_class(MESH_OT_create_spike)

    ## RIG ##
    bpy.utils.register_class(RIG_OT_controller_to_points)

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    ## UI ##
    bpy.utils.unregister_class(VIEW3D_PT_Organics_Generation)
    bpy.utils.unregister_class(VIEW3D_PT_Volume_Generation)
    bpy.utils.unregister_class(VIEW3D_PT_PlantGeneration)
    bpy.utils.unregister_class(NODE_PT_Organics_Generation)
    bpy.utils.unregister_class(NODE_PT_Volume)
    bpy.utils.unregister_class(NODE_PT_Plant_Generator)

    bpy.types.VIEW3D_HT_header.remove(draw_menu)
    bpy.utils.unregister_class(ORGANICS_MT_Menu)

    bpy.utils.unregister_class(NODE_OT_create_geometry_node)

    ## VOLUME ##
    bpy.utils.unregister_class(MESH_OT_hide_mesh)
    bpy.utils.unregister_class(MESH_OT_subdivision_mesh)

    ## PLANT ##
    bpy.utils.unregister_class(MESH_OT_create_leaf)
    bpy.utils.unregister_class(MESH_OT_create_spike)

    ## RIG ##
    bpy.utils.unregister_class(RIG_OT_controller_to_points)


if __name__ == "__main__":
    register()

### REGISTER END ###

"""
juju Julien BROUZES
https://github.com/Juju-brz
"""
