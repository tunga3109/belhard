from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='название',
        help_text='Макс. 64 символа'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация',
    )
    slug = models.SlugField(verbose_name='URL', unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'blog_categories' # название таблицы в бд
    
