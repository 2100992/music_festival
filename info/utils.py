from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from info.translater import translate
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


# class ObjectDetailMixin:
#     model = None
#     template = None

#     def get(self, request, slug):
#         obj = get_object_or_404(self.model, slug__iexact=slug)
#         context = {
#             self.model.__name__.lower(): obj
#         }

#         if request.user.is_authenticated:
#             context['username'] = request.user.username

#         return render(request, self.template, context=context)


# class ObjectsListMixin:
#     model = None
#     template = None
#     title = None


# ______________________________________________________________________
# utils for models


def make_unique_slug(model, text, counter=0):
    try:
        text = translate(text)
    except:
        print('Сервис перевода не доступен')
    slug = slugify(text)
    str_counter = ''
    # if slug == 'create':
    #     slug = 'create0'
    if counter:
        str_counter = str(counter)
    if model.objects.filter(slug=slug+str_counter).count():
        counter += 1
        slug = make_unique_slug(model, slug, counter)
    return slug + str_counter
