from django.http import HttpResponse


# ---------------------------------------------------------------------------- #
# healthcheck routes
# ---------------------------------------------------------------------------- #
def healthcheck():
    return HttpResponse("ok")


def index(request):
    return HttpResponse("Hello, world. You're at the sims core index.")
