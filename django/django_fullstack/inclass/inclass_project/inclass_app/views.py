from django.shortcuts import render, HttpResponse, redirect
from .models import Song

def index(request):
    print("In index method")
    return redirect("/songs")


def songs(request):
    print("In Songs")
    all_songs = Song.objects.all()
    print(all_songs)
    return render(request, "songs.html", {"songs": all_songs})

def new(request):
    print("In add")
    return render(request, "add.html")


def edit(request, song_id):
    print("In edit")
    return render(request, "edit.html")


def delete(request, song_id):
    print("In delete")
    return render(request, "delete.html")

def show(request, song_id):
    print("IN SHOW")
    return render(request,"show.html")

def create_process(request):
    print("in create process route", request.POST)
    Song.objects.create(title=request.POST['title'], artist=request.POST['artist'] )
    return redirect('/songs')

def update_process(request):
    print("in update process route", request.POST)
    return redirect('/songs')
