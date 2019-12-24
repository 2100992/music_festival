from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from committee.utils import GetContextDataMixin

from committee.models import Info
# Create your views here.

class Index(GetContextDataMixin, TemplateView):
    template_name = 'committee/index.html'
    # applicant_template_name = 'committee/applicant.html'
    # committeeman_template_name = 'committee/committeeman.html'
    model_info = Info
    destination = 'index'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('/')

        