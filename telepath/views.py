from django.shortcuts import render

from .models import Circle, Collage, Rectangle

def index(request):
    collage = Collage([
        Circle(30, 'red'),
        Rectangle(100, 50, 'yellow'),
    ])
    return render(request, 'index.html', {
        'collage': collage,
    })
