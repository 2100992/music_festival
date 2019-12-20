from django.db import models

from markdown import markdown
from slugify import slugify

from info.utils import make_unique_slug


class Info(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default='_',
        max_length=128,
        db_index=True,
        unique=True
    )
    markdown_field = models.TextField(
        null=True,
        blank=True
    )
    html_field = models.TextField(editable=False)
    destination = models.CharField(
        max_length=128,
        db_index=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, self.title)

        self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Participant(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default='_',
        max_length=128,
        db_index=True,
        unique=True
    )
    markdown_field = models.TextField(
        null=True,
        blank=True
    )
    html_field = models.TextField(editable=False)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, self.title)

        self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default='_',
        max_length=128,
        db_index=True,
        unique=True
    )
    markdown_field = models.TextField(
        null=True,
        blank=True
    )
    html_field = models.TextField(editable=False)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, self.title)

        self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
    )
    slug = models.SlugField(
        default='_',
        max_length=128,
        db_index=True,
        unique=True
    )
    img = models.ImageField(
        upload_to='info/gallery/%Y/%m/%d',
        blank=True,
        null=True,
    )
    remote_img = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    info = models.ForeignKey(
        Info,
        on_delete=models.CASCADE,
        related_name='gallery',
        blank=True,
        null=True
    )
    participant = models.ForeignKey(
        Participant,
        on_delete=models.CASCADE,
        related_name='gallery',
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='gallery',
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(self.__class__, self.title)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title