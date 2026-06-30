import bpy


#Still wip
def curve_rig():
    curve_obj = bpy.context.active_object
    #bpy.ops.object.armature_add()
    bpy.ops.object.editmode_toggle()

    spline = curve_obj.data.splines[0]
    points = spline.bezier_points
    n = 0
    number = spline.bezier_points[n]

    # for i, point in enumerate(points):
    # #for point in spline.bezier_points:
    # #for splines in curve_obj.data.splines:
    # #for i in range(curve_obj.data.spline):
    #     #bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value":(0, 0, 1)})
    #     #bpy.ops.object.hook_add_newob()
    #     print("points")
    #     #spline.bezier_points[n].select = True
    #     n = n + 1
    #     print(n)
    #     print(number)
    #
    #     #Select Vertice of Curve
    #     number.select_control_point = True
    #     number.select_left_handle = True
    #     number.select_right_handle = True
    #     number.bpy.ops.object.hook_add_newob()
    #
    #     #bpy.ops.curve.primitive_bezier_circle_add(()


    for point in spline.bezier_points:

        bpy.ops.curve.select_all(action='DESELECT')

        point.select_control_point = True
        point.select_left_handle = True
        point.select_right_handle = True

        bpy.context.view_layer.update()

        bpy.ops.object.hook_add_newob()
        bpy.ops.object.transforms_to_deltas(mode='ALL')





curve_rig()
