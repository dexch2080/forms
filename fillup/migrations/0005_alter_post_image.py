# Generated by Django 4.1.3 on 2022-12-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillup', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]