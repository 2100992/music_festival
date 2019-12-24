# Generated by Django 3.0 on 2019-12-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(default='_', max_length=128, unique=True)),
                ('markdown_field', models.TextField(blank=True, null=True)),
                ('html_field', models.TextField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('convetr_md_to_html', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(default='_', max_length=128, unique=True)),
                ('desctiption', models.TextField(blank=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
