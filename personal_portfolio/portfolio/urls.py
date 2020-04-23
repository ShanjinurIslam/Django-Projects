from django.urls import path
from blog import views as blog_views
from . import views


urlpatterns = [
    path('', views.home),
]
