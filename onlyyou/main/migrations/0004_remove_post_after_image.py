# Generated by Django 2.1.9 on 2019-08-13 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190813_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='after_image',
        ),
    ]