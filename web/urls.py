from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("pop-contact/", views.pop_contact, name="pop_contact"),
]
