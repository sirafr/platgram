"""POST URLS"""

# Django
from django.urls import path,include

# Views
from posts import views


urlpatterns = [
    path(
    route='',
    view = views.list_post,
    name='feed'),

    path(
        route ='posts/new', 
        view = views.create_post, 
        name='create'),
]