from django.shortcuts import render, get_object_or_404, redirect
from .models import Artwork
from . forms import ArtworkForm

# Create your views here.
def artwork_create(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('explore')
    else:
        form = ArtworkForm()
    return render(request, 'Artworks/artwork.html', {'form': form})

def artwork_update(request, pk):
    artwork = Artwork.object.get(pk=id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', pk=pk)
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'artworks/artwork_form.html', {'form': form})

def artwork_delete(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == 'POST':
        artwork.delete()
        return redirect('artwork_list')
    return render(request, 'artworks/artwork_confirm_delete.html', {'artwork': artwork})