from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0 # To set 0 emprty rows (thre by default)


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)