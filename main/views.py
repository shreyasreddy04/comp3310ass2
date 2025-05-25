from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
# Create your views here.
def home(request):
    query = request.GET.get("title")
    allMovies = None
    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        allMovies = Movie.objects.all()   # select * from movies
    #can use ,context dictionary instead {'movies': allMovies}
    return render(request, 'main/index.html', {'movies': allMovies}) #got error here, instead of using dictionary write in this way


# detail page
def details(request, id):
    movie = Movie.objects.get(id=id)
    # Retrieve reviews for the specific movie
    reviews = Review.objects.filter(movie=id).order_by("-comment")
    average = reviews.aggregate()
    return render(request, 'main/details.html', {'movie': movie, 'reviews': reviews})

# add movies to database
def add_movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None)
        # check if the form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:  # If it's not a POST request, render the empty form
        form = MovieForm()
        return render(request, 'main/addmovies.html', {"form": form})

#review
def add_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.movie = movie
            data.save()
            return redirect("main:details", id=id)
    else:
        form = ReviewForm()
        return render(request, 'main/details.html', {"movie": movie, "form": form})
