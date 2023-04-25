from django.urls import path
from . import views
urlpatterns = [
    path("form", views.index, name="index"),
    #path("base", views.base, name="contact")
]