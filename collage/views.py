from django.shortcuts import render

from .models import Collage
from .shapes import Circle, Rectangle

def index(request):
    collage = Collage([
        Circle(30, 'red'),
        Circle(50, 'blue'),
        Rectangle(100, 50, 'yellow'),
    ])
    return render(request, 'collage/index.html', {
        'collage': collage,
    })
