from django.db import models

from markdown import markdown
from slugify import slugify

from info.translater import translate


def make_unique_slug(model, text, counter=0):
    try:
        text = translate(text)
    except:
        print('Сервис перевода не доступен')
    slug = slugify(text)
    str_counter = ''
    if slug == 'create':
        slug = 'create0'
    if counter:
        str_counter = str(counter)
    if model.objects.filter(slug=slug+str_counter).count():
        counter += 1
        slug = make_unique_slug(model, slug, counter)
    return slug + str_counter


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
            self.slug = make_unique_slug(Info, self.title)

        self.html_field = markdown(self.markdown_field)

        super(Info, self).save(*args, **kwargs)

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
            self.slug = make_unique_slug(Participant, self.title)

        self.html_field = markdown(self.markdown_field)

        super(Participant, self).save(*args, **kwargs)

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
            self.slug = make_unique_slug(Location, self.title)

        self.html_field = markdown(self.markdown_field)

        super(Location, self).save(*args, **kwargs)

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
