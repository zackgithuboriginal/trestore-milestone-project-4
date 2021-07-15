from django.contrib import admin
from .models import ProgressPost, Comment


# Register your models here.
class CommentsAdmin(admin.TabularInline):
    model = Comment
    readonly_fields = ('date', 'author', 'post',)


class ProgressPostAdmin(admin.ModelAdmin):
    inlines = (CommentsAdmin,)

    list_display = (
        'post_title',
        'post_content',
        'date',
        'author',
        'image',
    )

    ordering = ('date',)


admin.site.register(ProgressPost, ProgressPostAdmin)
