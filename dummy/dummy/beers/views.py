# Create your views here.

from django.http import HttpResponse


def get_beers(request):
    return HttpResponse("Hello, world. You're at the polls index.")