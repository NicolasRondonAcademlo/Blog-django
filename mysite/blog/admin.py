from django.contrib import admin
from django.db import  models
# Register your models here.
from .models import Post
from pagedown.widgets import AdminPagedownWidget

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish', 'slug')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }