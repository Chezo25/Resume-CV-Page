from django.shortcuts import render

# Create your views here.


def home(request):
    return render(render, 'cvpage/templates/home.html')
