from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'is_published')
    list_editable = ('name', )
    list_filter = ('is_published', )
    prepopulated_fields = {'slug': ('name', )} # 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    ordering = ('date_created', '-title')
    list_display = ('title', 'full_name', 'date')
    list_filter = ('is_published', 'category') # боковая панель фильтрации
    fieldsets = (
        (
            'Основное',
            {
                'fields': ('title', 'descr', 'category'),
                'description': 'Основные значения'
            }
        ),
        
        (
            'Дополнительные', 
            {
                'fields': ('date_created', 'author', 'slug')
            }
        )
    )

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)
