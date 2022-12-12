from django.contrib import admin
from .models import Category, Post


@admin.action(description='опубликовать')
def make_published(self, request, queryset):  # выполняет запрос
    queryset.update(is_published=True)


@admin.action(description='снять с публикоации')
def make_unpublished(self, request, queryset):  # выполняет запрос
    queryset.update(is_published=False)


class ManagerPanel(admin.AdminSite):  # Панелька для менеджеров
    site_header = 'Manager Panel'
    site_title = 'manager'
    index_title = 'manager index'


manager = ManagerPanel(name='manager')


class PostInline(admin.StackedInline):
    model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ('id', 'name', 'is_published')
    inlines = (PostInline,)
    list_editable = ('name',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}  #


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    search_fields = ('title',)
    search_help_text = 'Поиск по заголовку'
    ordering = ('date_created', '-title')
    list_display = ('title', 'full_name', 'date')
    readonly_fields = ('date_created', 'slug')  # атрибуты, которые нельзя редактировать
    list_filter = ('is_published', 'category')  # боковая панель фильтрации
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
manager.register(Category, CategoryAdmin)
manager.register(Post, PostAdmin)
