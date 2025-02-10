import bpy

#オペレータ ICO球作成
class MYADDON_OT_create_ico_sphere(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_object"
    bl_label = "ICO球作成"
    bl_description = "ICO球作成を生成します"
    #redo,undo可能オプション
    bl_options = {"REGISTER", "UNDO"}

    #メニューを実行したときに呼ばれるコールバック関数
    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("ICO球作成を生成しました。")
        return {'FINISHED'}