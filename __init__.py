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
from .add_filename import MYADDON_OT_add_filename
from .DrawCollider import DrawCollider
from .add_collider import MYADDON_OT_add_collider
from .my_menu import TOPBAR_MT_my_menu
from .file_name import OBJECT_PT_file_name
from .collider import OBJECT_PT_collider
from .disabled import MYADDON_OT_add_disabled
from .disabled import OBJECT_PT_disabled

#アドオン有効化時コールバック
def register():
    # Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)
    #メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    # 3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました。")

#アドオン無効化時コールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    
    # Blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました。")

#テスト用実行コード
if __name__ == "__main__":
    register()

# メニュー項目描画
def draw_menu_manual(self, context):
    self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')

# Blenderに登録するクラスリスト
classes = (
    TOPBAR_MT_my_menu,
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    MYADDON_OT_export_scene,
    MYADDON_OT_add_filename,
    MYADDON_OT_add_collider,
    MYADDON_OT_add_disabled,
    OBJECT_PT_file_name,
    OBJECT_PT_collider,
    OBJECT_PT_disabled,
)
