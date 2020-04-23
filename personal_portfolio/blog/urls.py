from django.urls import path
from blog import views as blog_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home),
    path('<int:blog_id>', views.detail,name='detail'),
]
