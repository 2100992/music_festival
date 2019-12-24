from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Index(TemplateView):
    pass
    # template_name = 'committee/index.html'
    # # applicant_template_name = 'committee/applicant.html'
    # # committeeman_template_name = 'committee/committeeman.html'
    # model_info = Info
    # destination = 'index'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return super().dispatch(request, *args, **kwargs)
    #     else:
    #         return redirect('/')

        