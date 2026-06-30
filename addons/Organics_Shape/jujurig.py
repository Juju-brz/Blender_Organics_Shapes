import bpy


def curve_rig():
    curve_obj = bpy.context.active_object
    bpy.ops.object.armature_add()
    bpy.ops.object.editmode_toggle()

    spline = curve_obj.data.splines[0]  # ✅ .data.splines (pas .spline)
    points = spline.bezier_points

    for i, point in enumerate(points):
    #for point in spline.bezier_points:
    #for splines in curve_obj.data.splines:
    #for i in range(curve_obj.data.spline):
        bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value":(0, 0, 1)})
        #bpy.ops.object.hook_add_newob()
        print("points")

        #bpy.ops.curve.primitive_bezier_circle_add(()



    bpy.ops.object.editmode_toggle()

