from django.urls import path
from .views import post_requests


urlpatterns = [
    path('v1/post/', post_requests, name='post_request')   # POST API
]
