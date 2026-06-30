import bpy


#Still wip
def curve_rig():
    curve = bpy.context.active_object

    bpy.ops.object.mode_set(mode='EDIT')

    spline = curve.data.splines[0]

    for i in range(len(spline.bezier_points)):

        bpy.ops.curve.select_all(action='DESELECT')

        # Sélectionne uniquement le point i
        spline.bezier_points[i].select_control_point = True
        spline.bezier_points[i].select_left_handle = True
        spline.bezier_points[i].select_right_handle = True

        bpy.context.view_layer.update()

        try:
            bpy.ops.object.hook_add_newob()
            bpy.ops.object.transforms_to_deltas(mode='ALL')
        except RuntimeError as e:
            print(f"Erreur au point {i} :", e)
            break

    bpy.ops.object.mode_set(mode='OBJECT')




