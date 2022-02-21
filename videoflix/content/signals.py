from django.dispatch import receiver
from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print('Video saved')
    if created: 
        print('New Video created')

# post_save.connect(video_post_save, sender=Video)