from django.contrib import admin
from .models import ProgressPost

# Register your models here.

class ProgressPostAdmin(admin.ModelAdmin):
    list_display = (
        'post_title',
        'post_content',
        'date',
        'author',
        'image',
    )

    ordering = ('date',)


admin.site.register(ProgressPost, ProgressPostAdmin)
