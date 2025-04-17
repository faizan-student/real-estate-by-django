from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, Http404
from .models import Project
from .utils import generate_presigned_url
from django.db import connections


class Home(TemplateView):
    template_name = "html/home.html"


class Projects(TemplateView):
    template_name = "html/projects.html"

    def get_context_data(self, **kwargs):
        print("Inside get_context_data")
        try:
            # Check if the connection to MongoDB is active
            connections["default"].cursor()
            print("MongoDB connection is active")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()

        # Add additional print statements for debugging
        print("Projects fetched:", context["projects"])
        return context


class SearchProperty(TemplateView):
    template_name = "html/search-property.html"


class Finance(TemplateView):
    template_name = "html/finance.html"


class AboutUs(TemplateView):
    template_name = "html/about-us.html"


class Blogs(TemplateView):
    template_name = "html/blogs.html"


def download_brochure(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("Project not found")

    # Extract bucket and key from s3 URI
    s3_uri = project.broucher_url
    if not s3_uri.startswith("s3://"):
        raise ValueError("Invalid S3 URI format")

    s3_uri_parts = s3_uri.replace("s3://", "").split("/", 1)
    bucket_name = s3_uri_parts[0]
    s3_key = s3_uri_parts[1]

    presigned_url = generate_presigned_url(bucket_name, s3_key)

    return JsonResponse({"url": presigned_url})
