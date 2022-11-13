from django.contrib import admin
from .models import Book, Chapter, Content_Chapter, Category

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    """docstring for BookAdmin"""
    list_display = ('id', 'slug', 'name_book', 'author', 'content_summary', 'illumination', 'upload_by', 'uploaded_at', 'updated_by', 'updated_at', 'status')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug_chapter', 'book', 'name_chapter', 'created_by', 'created_at', 'updated_at')

    class Meta:
        verbose_name = "ChapterAdmin"
        verbose_name_plural = "ChapterAdmins"

    pass


# class ContentChapterAdmin(admin.ModelAdmin):
#     '''
#         Admin View for ContentChapter
#     '''
#     list_display = ('id', 'chapter', 'content_chapter', 'last_updated')
#     # list_filter = ('',)
#     # inlines = [
#     #     Inline,
#     # ]
#     # raw_id_fields = ('',)
#     # readonly_fields = ('',)
#     # search_fields = ('',)


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('name_category', )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


admin.site.register(Category, CategoryAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Content_Chapter, ContentChapterAdmin)
