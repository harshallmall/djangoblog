from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content_text = models.TextField()
    date_posted = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.title
