import bpy

class ORGANICS_MT_Menu(bpy.types.Menu):
    bl_label = "Organics"
    bl_idname = "ORGANICS_MT_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Organic Tools", icon='PARTICLES')
        layout.separator()
        layout.operator("organics.scatter", text="Scatter", icon='STICKY_UVS_VERT')
        layout.operator("organics.branch",  text="Branch Generator", icon='OUTLINER_OB_CURVE')
        layout.operator("organics.leaf",    text="Leaf Distribution", icon='FORCE_WIND')
        layout.label(text="truc")

def draw_menu(self, context):
    self.layout.separator()
    self.layout.menu("ORGANICS_MT_menu", text="Organics", icon='OUTLINER_OB_POINTCLOUD')

def register():
    bpy.utils.register_class(ORGANICS_MT_Menu)
    bpy.types.VIEW3D_HT_header.append(draw_menu)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw_menu)
    bpy.utils.unregister_class(ORGANICS_MT_Menu)

# 👇 Ces 2 lignes manquaient !
if __name__ == "__main__":
    register()
