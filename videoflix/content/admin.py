from django.contrib import admin

from .models import Video

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    fields = ('created_at', 'title', 'description', 'video_file')
    list_display = ('created_at', 'title')
    search_fields = ('title',)

admin.site.register(Video, VideoAdmin)