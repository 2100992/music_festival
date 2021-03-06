from django.db import models
from django.utils import timezone

from markdown import markdown

from .utils import make_unique_slug
from .translater import translate

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        default="_",
        db_index=True,
        unique=True
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ('D', 'draft'),
            ('P', 'published')
        ],
        default='D',
    )
    markdown_field = models.TextField(
        null=True,
        blank=True
    )
    html_field = models.TextField(
        null=True,
        blank=True
    )
    updated = models.DateTimeField(
        default=timezone.now
    )
    publication_date = models.DateTimeField(
        default=timezone.now
    )
    convetr_md_to_html = models.BooleanField(default=True)

    class Meta:
        ordering = ['publication_date']

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, f'{self.publication_date.strftime("%d/%m/%y")}-{translate(self.title)}')

        if self.convetr_md_to_html:
            self.convetr_md_to_html = False
            self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        default="_",
        db_index=True,
        unique=True
    )
    post = models.ManyToManyField(
        Post,
        related_name='category',
    )

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title