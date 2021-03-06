from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from committee.translater import translate
from slugify import slugify
from markdown import markdown

# ______________________________________________________________________
# utils for views


class GetContextDataMixin:
    model_info = None
    model = None
    destination = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {}

        context['info'] = get_list_or_404(
            self.model_info, destination=self.destination)

        context['title'] = context['info'][0].title

        if self.model:
            context[self.destination] = self.model.objects.all()

        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username

        return context

# ______________________________________________________________________
# utils for models


def make_unique_slug(model, text):
    slug = slugify(text)
    counter = 0
    str_counter = ''

    while model.objects.filter(slug=slug+str_counter).count():
        print(slug+str_counter)
        counter += 1
        str_counter = str(counter)
    return slug + str_counter