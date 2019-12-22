# Generated by Django 3.0 on 2019-12-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20191222_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='convetr_md_to_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='convetr_md_to_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='html_field',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='html_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]