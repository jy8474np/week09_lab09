from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid:
            place.save()
            return redirect('place_list')

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places , 'new_place_form' : new_place_form})

def about(request):
    author = 'Michael Lynch'
    about = 'A website to create list of places to visit.'
    return render(request , 'travel_wishlist/about.html' , {'author' : author , 'about' : about})
