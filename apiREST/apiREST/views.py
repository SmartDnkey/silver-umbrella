from django.http import HttpResponse


def main(request):
    return HttpResponse("Hello, world! This is a simple Django app")