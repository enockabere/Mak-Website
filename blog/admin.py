from django.contrib import admin
from blog.models import Post,Category, Featured
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'

    fields = ('image', 'title', 'slug', 'content',
              'author', 'category', 'blog_photo', 'status')

    list_display = [
        'blog_photo',
        'title',
        'short_description',
        'status',
        'author',
        'created_on',
    ]
    list_display_links = ['title']
    list_filter = ["status", 'created_on', 'category']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['blog_photo', 'created_on', ]
    

class FeaturedAdmin(admin.ModelAdmin):
    list_filter = ['status', 'created_on']
    list_display_links = ['title']
    list_display = [
        'photo',
        'title',
        'created_on',
        'status',
    ]
    search_fields = ['title',]



# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Featured, FeaturedAdmin)

