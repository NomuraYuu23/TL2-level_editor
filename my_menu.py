import bpy

#ブレンダーに登録するアドオン情報
bl_info = {
    "name" : "レベルエディタ",
    "author" : "Yu Nomura",
    "version" : (1, 0),
    "blender" : (3, 3, 1),
    "Location" : "",
    "description" : "レベルエディタ",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Object"
}

# モジュールのインポート
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .spawn import MYADDON_OT_spawn_create_symbol

#トップバーの拡張メニュー
class TOPBAR_MT_my_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_my_menu"
    bl_label = "MyMenu"
    bl_description = "拡張メニュー by " + bl_info["author"]

    #描画
    def draw(self,context):
        self.layout.operator("wm.url_open_preset",
                              text="Manual", icon='HELP')
        self.layout.separator()
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,
                              text=MYADDON_OT_stretch_vertex.bl_label)
        self.layout.separator()
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,
                              text=MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.separator()
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,
                              text=MYADDON_OT_export_scene.bl_label)
        self.layout.separator()
        self.layout.operator(MYADDON_OT_spawn_create_symbol.bl_idname,
                              text=MYADDON_OT_spawn_create_symbol.bl_label)

    #既存のメニューの描画
    def submenu(self, context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)
