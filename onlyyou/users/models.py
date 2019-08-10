from django.db import models
from django.contrib.auth.models import User
import os


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profile/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_image = models.FileField(default='first_image.jpg', upload_to=user_directory_path)
    second_image = models.FileField(default='second_image.jpg', upload_to=user_directory_path)
    third_image = models.FileField(default='third_image.jpg', upload_to=user_directory_path)
    #upload = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        #
        # img_1 = Image.open(self.first_image.path)
        # img_1.save(first_image. .path)
        # img_2 = Image.open(self.second_image.path)
        # img_2.save(img_2.path)
        # img_3 = Image.open(self.third_image.path)
        # img_3.save(img_3.path)

