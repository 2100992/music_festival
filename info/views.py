from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Musicians(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Scenes(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
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

class Location(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)

class Contacts(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)