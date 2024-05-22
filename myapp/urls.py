from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     path('', views.HomeView.as_view(), name = 'home'),
     path('about/', views.AboutMe.as_view(), name = 'about'),
     path('detail/<int:pk>', views.BlogDetailView.as_view(), name = 'detail'),
     path('list/', views.BlogListView.as_view(), name = 'list'),
     path('gallery/', views.GalleryView.as_view(), name='photo_gallery'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)