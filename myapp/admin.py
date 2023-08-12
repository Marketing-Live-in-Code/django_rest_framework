from django.contrib import admin

# Register your models here.
# 加入以下程式碼
from myapp.models import Article, Classification

admin.site.site_header = '行銷搬進大程式' # 網站大標題
admin.site.index_title = '後台管理' # 副標題
admin.site.site_title = '行銷搬進大程式後台' # 瀏覽器上方title

class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','title','language','classification_id','created_time'] # 設定要在在列表頁面顯示的欄位
    list_filter=['classification_id',] # 設定欄位啟用列表頁面右側的篩選器
    search_fields=['title'] # 設定列表頁面的搜尋框，可以使用欄位名稱或是關聯欄位名稱 API
    ordering=['-created_time']
    list_per_page=10
admin.site.register(Article, ArticleAdmin)

class ClassificationAdmin(admin.ModelAdmin):
    list_display=['id','title','created_time'] # 設定要在在列表頁面顯示的欄位
    list_filter=['title',] # 設定欄位啟用列表頁面右側的篩選器
    search_fields=['title'] # 設定列表頁面的搜尋框，可以使用欄位名稱或是關聯欄位名稱 API
    ordering=['-created_time']
    list_per_page=10
admin.site.register(Classification, ClassificationAdmin)