# Generated by Django 4.1.3 on 2022-12-01 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fillup', '0002_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
