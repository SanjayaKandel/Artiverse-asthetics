from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from Artworks.models import Artwork

# Create your views here.
def index(request):
    return render(request, 'Home/index.html')

def explore(request):
    arts = Artwork.objects.all()
    context = {
        'arts': arts
    }
    return render(request, 'Home/explore.html', context)


def search(request):
    query = request.GET.get('query', '')
    medium = request.GET.get('medium', '')

    if medium:
        result = Artwork.objects.filter(
            title__icontains=query,
            medium__icontains=medium
        )
    else:
        result = Artwork.objects.filter(
            title__icontains=query
        )

    context = {
        'result': result,
        'query': query,
    }
    return render(request, 'Home/search.html', context)