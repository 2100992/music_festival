from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class Index(TemplateView):
    template_name = 'committee/index.html'