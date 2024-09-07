from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("healthcheck/", views.healthcheck, name="healthcheck"),
    path("traits/", views.traits, name="traits"),
    path("careers/", views.careers, name="careers"),
    path("aspirations/", views.aspirations, name="aspirations")
]
