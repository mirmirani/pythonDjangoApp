# howdy/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

# create your views here

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = 'about.html'

"""
Notice that in the second view, I did not define a get method. This is just another way of using the TemplateView class. If you set the template_name attribute, a get request to that view will automatically use the defined template. Try changing the HomePageView to use the format used in AboutPageView.
"""
