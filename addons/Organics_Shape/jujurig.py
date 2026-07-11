import bpy


#Still wip
def controller_to_points():

    rig_collection = bpy.data.collections.new("Rig")
    bpy.context.scene.collection.children.link(rig_collection)


    curve = bpy.context.active_object

    bpy.ops.object.mode_set(mode='EDIT')
    spline = curve.data.splines[0]

    #rig_collection.objects.link(bpy.context.active_object)
    for i in range(len(spline.bezier_points)):

        bpy.ops.curve.select_all(action='DESELECT')

        # Sélectionne uniquement le point i
        spline.bezier_points[i].select_control_point = True
        spline.bezier_points[i].select_left_handle = True
        spline.bezier_points[i].select_right_handle = True

        bpy.context.view_layer.update()

        try:
            #bone = edit_bones.new(f"Bone_{i:02d}")
            bpy.ops.object.hook_add_newob()
            hook_mod = curve.modifiers[-1]
            empty = hook_mod.object
            empty.name = f"CTRL_point_{i:02d}" #RENAME

            obj = bpy.ops.object.transforms_to_deltas(mode='ALL')
            #obj.name = f"RIG_curve_points{i}"
        except RuntimeError as e:
            print(f"Erreur au point {i} :", e)
            break

    bpy.ops.object.mode_set(mode='OBJECT')


def curve_to_bones():

    # VARIABLES
    curve = bpy.context.active_object
    if curve.type != 'CURVE':
        print("Select a curve")
        return


    spline = curve.data.splines[0]
    points = spline.bezier_points


    curve_matrix = curve.matrix_world
    positions = [curve_matrix @ p.co for p in points]

    # Create Collection
    rig_collection = bpy.data.collections.new("Rig")
    bpy.context.scene.collection.children.link(rig_collection)


    armature_data = bpy.data.armatures.new("RigArmature")
    armature_data.display_type = 'BBONE'

    # Rename
    armature_obj = bpy.data.objects.new("RigArmature", armature_data)
    rig_collection.objects.link(armature_obj)

    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='EDIT')

    edit_bones = armature_data.edit_bones
    bone_names = []
    #bone.bbone_segments = 6



    for i in range(len(positions) - 1):
        bone = edit_bones.new(f"Bone_{i:02d}")
        bone.head = positions[i]
        bone.tail = positions[i + 1]

        if i > 0:
            bone.parent = edit_bones[bone_names[i - 1]]
            bone.use_connect = True

        bone_names.append(bone.name)

    bpy.ops.object.mode_set(mode='OBJECT')


    bpy.ops.object.mode_set(mode='POSE')

    last_bone = armature_obj.pose.bones[bone_names[-1]]
    constraint = last_bone.constraints.new('SPLINE_IK')
    constraint.target = curve
    constraint.chain_count = len(bone_names)

    bpy.ops.object.mode_set(mode='OBJECT')

    return armature_obj




