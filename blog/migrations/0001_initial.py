# Generated by Django 3.0 on 2019-12-26 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='_', unique=True)),
                ('status', models.CharField(choices=[('D', 'draft'), ('P', 'published')], max_length=10)),
                ('markdown_field', models.TextField(blank=True, null=True)),
                ('html_field', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('convetr_md_to_html', models.BooleanField(default=False)),
            ],
        ),
    ]
