from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, "hello.html", {"name" : "Jaison"})
    # return render(request) - Will fail since the template name is required