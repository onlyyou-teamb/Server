from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profile/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_image = models.FileField(
        default='first_image.jpg', upload_to=user_directory_path)
    second_image = models.FileField(
        default='second_image.jpg', upload_to=user_directory_path)
    third_image = models.FileField(
        default='third_image.jpg', upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

    @classmethod
    def create(cls, user):
        Profile = cls(user=user)

        return Profile
