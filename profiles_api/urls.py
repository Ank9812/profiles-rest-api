"""
In Django, urls.py is a Python module that defines the URL patterns for your
application. It is typically located in the application directory alongside
other Python modules such as views.py, models.py, and forms.py.

The urls.py module maps URLs to views, which are Python functions or classes
that handle HTTP requests and return HTTP responses. The URL patterns are
defined using regular expressions or string patterns that match the
requested URL.
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


















urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
