from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView)
from .models import Blog, PhotoGallery


class HomeView(TemplateView):
    template_name = 'base.html'

class AboutMe(TemplateView):
    template_name = 'about.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

class BlogListView(ListView):
    model = Blog
    template_name = 'list.html'

    def get_queryset(self):
        return Blog.objects.filter(published_on__lte = timezone.now()).order_by('-published_on')
    
class GalleryView(ListView):
    model = PhotoGallery
    template_name = 'gallery.html'
    context_object_name = 'photo_list'
    def get_queryset(self):
        return PhotoGallery.objects.all()