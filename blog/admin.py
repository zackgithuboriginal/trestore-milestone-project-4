from django.contrib import admin
from .models import ProgressPost, Comment


class CommentsAdmin(admin.TabularInline):
    """
    Admin config for Comments
    Specifies that all fields but the post content are
    readonly
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
