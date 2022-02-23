from pyexpat import model
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Video

# Register your models here.

class VideoResource(resources.ModelResource):
    class Meta:
        model: Video

@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    # fields = ('created_at', 'title', 'description', 'video_file')
    # list_display = ('created_at', 'title')
    # search_fields = ('title',)
    pass