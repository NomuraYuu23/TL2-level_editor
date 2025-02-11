import bpy

#オペレータ 無効オプションを追加する
class MYADDON_OT_add_disabled(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_disabled"
    bl_label = "disabled 追加"
    bl_description = "['disabled']カスタムプロパティを追加します"
    bl_options = {"REGISTER", "UNDO"}

    #メニューを実行したときに呼ばれるコールバック関数
    def execute(self, context):
        #['disabled']カスタムプロパティを追加
        context.object["disabled"] = True

        return {'FINISHED'}

        
# パネル コライダー
class OBJECT_PT_disabled(bpy.types.Panel):
    bl_idname = "OBJECT_PT_disabled"
    bl_label = "Disabled"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    # サブメニューの描画
    def draw(self, context):
        # パネルに項目を追加
        if "disabled" in context.object:
            # 既にプロパティがあればプロパティを表示
            self.layout.prop(context.object, '["disabled"]', text = "disabled")
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_disabled.bl_idname)
    
        return {'FINISHED'}
