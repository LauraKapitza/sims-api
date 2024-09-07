from django.http import HttpResponse
from django.shortcuts import render

from sims.core.models import Trait, Career, Aspiration


# ---------------------------------------------------------------------------- #
# healthcheck routes
# ---------------------------------------------------------------------------- #
def healthcheck():
    return HttpResponse("ok")


def index(request):
    return render(request, "home.html")


def traits(request):
    trait_list = Trait.objects.order_by("name")
    context = {
        "list": trait_list,
        "title": "Traits"
    }
    return render(request, "list.html", context)


def careers(request):
    career_list = Career.objects.order_by("name")
    context = {
        "list": career_list,
        "title": "Careers"
    }
    return render(request, "list.html", context)


def aspirations(request):
    aspiration_list = Aspiration.objects.order_by("name")
    context = {
        "list": aspiration_list,
        "title": "Aspirations"
    }
    return render(request, "list.html", context)