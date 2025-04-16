from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "html/home.html"


class Projects(TemplateView):
    template_name = "html/projects.html"


class SearchProperty(TemplateView):
    template_name = "html/search-property.html"


class Finance(TemplateView):
    template_name = "html/finance.html"


class AboutUs(TemplateView):
    template_name = "html/about-us.html"


class Blogs(TemplateView):
    template_name = "html/blogs.html"



