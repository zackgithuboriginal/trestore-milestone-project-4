from django.contrib import admin
from .models import ProgressPost, Comment


class CommentsAdmin(admin.TabularInline):
    """
    Admin config for Commens
    Specifies that all but the post content are
    readonly fields
    """
    model = Comment
    readonly_fields = ('date', 'author', 'post',)


class ProgressPostAdmin(admin.ModelAdmin):
    """
    Admin config for Progress Posts
    Displays all fields for post object
    and all attached comments as inline elements
    """
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
