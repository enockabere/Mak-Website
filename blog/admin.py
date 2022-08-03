from unicodedata import category
from django.contrib import admin
from blog.models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
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
    # actions = [Publish,Unpublish]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)

