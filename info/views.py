from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    template = 'info/index.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template, context=context)