from django.urls import path
from .views import *

urlpatterns = [
    path("home/", Home.as_view()),
    path("projects/", Projects.as_view()),
    path("search-properties/", SearchProperty.as_view()),
    path("finance/", Finance.as_view()),
    path("about-us/", AboutUs.as_view()),
    path("blogs/", Blogs.as_view()),
]
