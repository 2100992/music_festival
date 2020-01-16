from allauth.account.views import LoginView, LogoutView, SignupView
from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView

from .models import Info, Participant, Location, Photo
from .utils import GetContextDataMixin
from .utils import ObjectDetailMixin, ObjectsListMixin
from .utils import print_user_info

from blog.models import Post, Category
from .forms import UserLoginForm, UserSignupForm

from allauth.account.forms import SignupForm

from django.contrib.auth.models import User


# Create your views here.

class SmallTest(View):
    template = 'info/small_test.html'

    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

    def post(self, request):
        pass


class LoginViewClass(LoginView):
    template_name = "info/login.html"
    form_class = UserLoginForm
    success_url = None
    redirect_field_name = "next"


class LogoutViewClass(LogoutView):
    template_name = "info/logout.html"


class SignupViewClass(SignupView):
    template_name = "info/login.html"
    form_class = UserSignupForm


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
    destination = 'infrastructure'


class Contacts(GetContextDataMixin, TemplateView):
    template_name = 'info/contacts.html'
    model_info = Info
    destination = 'contacts'


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


class BlogPosts(View):
    template = 'info/blog.html'

    def get(self, request):
        context = {}
        context['posts'] = Post.objects.all()

        if request.user.is_authenticated:
            context['username'] = request.user.username

        return render(request, self.template, context=context)


class BlogPostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'info/blog.html'


class BlogCategories(View):
    template = 'info/blog.html'

    def get(self, request):
        context = {}
        context['categories'] = Category.objects.all()

        if request.user.is_authenticated:
            context['username'] = request.user.username

        return render(request, self.template, context=context)


class BlogCategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'info/blog.html'


def profile_redirect(request):
    print()
    print('User logged in')
    print_user_info(request)
    if request.user.is_authenticated:
        groups = set(group.name for group in request.user.groups.all())
        if request.user.is_superuser:
            return redirect('/admin/')
        elif 'Applicant' in groups:
            return redirect(reverse('committee:applicant_url'))
        elif 'Committeeman' in groups:
            return redirect(reverse('committee:committeeman_url'))
    return redirect('/')


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
