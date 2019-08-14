from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/posts/{1}'.format(instance.author, filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    before_image = models.FileField(
        default='before_image.jpg', upload_to=user_directory_path)
    after_image = models.FileField(
        default='after_image.jpg', upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
