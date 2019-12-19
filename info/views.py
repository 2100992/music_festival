from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from info.models import Info, Participant, Location
from django.shortcuts import get_object_or_404, get_list_or_404



# Create your views here.


# class Index(View):
#     template = 'info/index.html'
#     model_info = Info
    
#     def get(self, request):
#         context = {}
#         context['info'] = get_object_or_404(self.model_info, destination='index')
#         return render(request, self.template, context=context)


class Index(TemplateView):
    template_name = 'info/index.html'
    model_info = Info

    def get_context_data(self, **kwargs):
        context = {}
        context['info'] = get_object_or_404(self.model_info, destination='index')
        return context


class Participans(View):
    template = 'info/participants.html'
    model_info = Info
    model = Participant
    
    def get(self, request):
        context = {}
        context['info'] = get_object_or_404(self.model_info, destination='participants')
        context['participants'] = Participant.objects.all()
        return render(request, self.template, context=context)

class Locations(View):
    template = 'info/locations.html'
    model_info = Info
    model = Location
    
    def get(self, request):
        context = {}
        context['info'] = get_object_or_404(self.model_info, destination='locations')
        context['locations'] = Location.objects.all()
        return render(request, self.template, context=context)

class Gallery(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Blog(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Road(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Infrastructure(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Contacts(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)


# class Login(LoginView):
#     template_name = 'p_library/login.html'

#     def get_success_url(self):
#         url = self.get_redirect_url()
#         if url:
#             return url
#         elif self.request.user.is_superuser:
#             return '/admin/'
#             # return reverse('admin')   # почему-то не работает
#         else:
#             return reverse('p_library:library_url')