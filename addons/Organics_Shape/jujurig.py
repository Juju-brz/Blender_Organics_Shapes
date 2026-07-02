import bpy


#Still wip
def controller_to_points():
    rig_collection = bpy.data.collections.new("Rig")
    bpy.context.scene.collection.children.link(rig_collection)
    curve = bpy.context.active_object
    #rig_collection.objects.link(bpy.context.active_object)

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
            bpy.ops.object.hook_add_newob()
            obj = bpy.context.active_object
            obj = bpy.ops.object.transforms_to_deltas(mode='ALL')
            #obj.name = f"RIG_curve_points{i}"
        except RuntimeError as e:
            print(f"Erreur au point {i} :", e)
            break

    bpy.ops.object.mode_set(mode='OBJECT')




