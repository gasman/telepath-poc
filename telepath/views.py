from django.shortcuts import render

from .models import Circle, Collage, Rectangle

def index(request):
    collage = Collage([
        Circle(100, 'red'),
        Rectangle(100, 50, 'green'),
    ])
    return render(request, 'index.html', {
        'collage': collage,
    })
