# Generated by Django 3.0 on 2019-12-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20191220_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='convetr_md_to_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='info',
            name='html_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
