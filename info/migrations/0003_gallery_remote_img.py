# Generated by Django 3.0 on 2019-12-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20191218_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='remote_img',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
