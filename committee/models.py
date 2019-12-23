from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from committee.utils import make_unique_slug
from committee.translater import translate

# Create your models here.

class Applicant(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True
    )
    slug = models.SlugField(
        default="_",
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
    convetr_md_to_html = models.BooleanField(
        default=False
    )
    is_adopted = models.BooleanField(
        default=False
    )
    
    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = make_unique_slug(self.__class__, translate(self.title))

        if self.convetr_md_to_html:
            self.convetr_md_to_html = False
            self.html_field = markdown(self.markdown_field)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Committeeman(models.Model):
    nickname = models.CharField(
        max_length=128,
        db_index=True,
        unique=True
    )
    signature = models.CharField(
        max_length=128,
        db_index=True,
        unique=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='committeeman',
        blank=True,
        null=True
    )
    vote = models.ManyToManyField(
        Applicant,
        blank=True,
        related_name='committeeman'
    )
    def __str__(self):
        return self.nickname

class Message(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True
    )
    slug = models.SlugField(
        default="_",
        max_length=128,
        db_index=True,
        unique=True
    )
    desctiption = models.TextField(
        null=True,
        blank=True
    )
    date_time = models.DateTimeField(
        auto_now=False,
        auto_now_add=True)