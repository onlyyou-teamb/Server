# Generated by Django 2.2.3 on 2019-08-12 17:20

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190810_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_image',
            field=models.FileField(default='first_image.jpg', upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_image',
            field=models.FileField(default='second_image.jpg', upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='third_image',
            field=models.FileField(default='third_image.jpg', upload_to=users.models.user_directory_path),
        ),
    ]
