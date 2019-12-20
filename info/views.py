from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from info.models import Info, Participant, Location, Photo
from django.shortcuts import get_object_or_404, get_list_or_404
from info.utils import GetContextDataMixin


# Create your views here.


class Index(GetContextDataMixin, TemplateView):
    template_name = 'info/index.html'
    model_info = Info
    destination = 'index'


class Participans(GetContextDataMixin, TemplateView):
    template_name = 'info/participants.html'
    model_info = Info
    model = Participant
    destination = 'participants'


class Locations(GetContextDataMixin, TemplateView):
    template_name = 'info/locations.html'
    model_info = Info
    model = Location
    destination = 'locations'


class Road(GetContextDataMixin, TemplateView):
    template_name = 'info/road.html'
    model_info = Info
    destination = 'road'


class Infrastructure(GetContextDataMixin, TemplateView):
    template_name = 'info/infrastructure.html'
    model_info = Info
    destination='infrastructure'


class Contacts(GetContextDataMixin, TemplateView):
    template_name = 'info/contacts.html'
    model_info = Info
    destination='contacts'


class Gallery(GetContextDataMixin, TemplateView):
    template_name = 'info/gallery.html'
    model_info = Info
    model = Photo
    destination = 'gallery'

    # def get_context_data(self, **kwargs):
    #     context = {}
    #     context['img'] = self.model.objects.all()

    #     context['info'] = get_list_or_404(
    #         self.model_info, destination=self.destination)
        
    #     context['title'] = context['info'][0].title

    #     if self.model:
    #         context[self.destination] = self.model.objects.all()

    #     return context


class Blog(View):
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
