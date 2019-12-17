from django.db import models

# Create your models here.

class Musician(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default=' ',
        max_length=128,
        db_index=True,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

class Gallery(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default=' ',
        max_length=128,
        db_index=True,
        unique=True
    )
    img = models.ImageField(
        upload_to='info/gallery/%Y/%m/%d',
        blank=True,
        null=True,
    )
    musician = models.ForeignKey(
        Musician,
        on_delete = models.CASCADE,
        related_name='gallery',
        blank=True,
        null=True
    )

class Scene(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default=' ',
        max_length=128,
        db_index=True,
        unique=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )