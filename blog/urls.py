from django.urls import path
from blog.apps import BlogConfig
from blog.views import home

app_name = BlogConfig.name

urlpatterns = [
    path('', home, name='home'),
]
