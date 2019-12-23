from django.db import models

from markdown import markdown

from info.translater import translate
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
    html_field = models.TextField(
        null=True,
        blank=True
    )
    destination = models.CharField(
        max_length=128,
        db_index=True,
        null=True,
        blank=True
    )

    convetr_md_to_html = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        if self.convetr_md_to_html:
            self.convetr_md_to_html = False
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
    html_field = models.TextField(
        null=True,
        blank=True
    )

    convetr_md_to_html = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        if self.convetr_md_to_html:
            self.convetr_md_to_html = False
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
    html_field = models.TextField(
        null=True,
        blank=True
    )

    convetr_md_to_html = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        if self.convetr_md_to_html:
            self.convetr_md_to_html = False
            self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Photo(models.Model):
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
        related_name='photo',
        blank=True,
        null=True
    )
    participant = models.ForeignKey(
        Participant,
        on_delete=models.CASCADE,
        related_name='photo',
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='photo',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
