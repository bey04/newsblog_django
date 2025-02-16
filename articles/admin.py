from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class Commentline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [Commentline]



admin.site.register(Article, ArticleAdmin)    
admin.site.register(Comment)