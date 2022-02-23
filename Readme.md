# Issues

Backend
-Signals
 Add Delete
 Video Converter post_create signal to trigger a callback after the video has been converted

-If Import Export not working
https://stackoverflow.com/questions/43419721/django-import-export-not-showing-in-admin

-Docs
https://django-import-export.readthedocs.io/en/latest/getting_started.html
-python manage.py shell
>>> from app.admin import ModelResource
>>> dataset = ModelResource().export() AttributeError: 'NoneType' object has no attribute 'objects'

django.db.utils.OperationalError: no such table: users_customuser