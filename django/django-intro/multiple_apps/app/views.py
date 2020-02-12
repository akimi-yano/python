from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
    
def makething(request):
    print("in create")
    return redirect("/blogs")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")
    
def destroy(request, number):
    return redirect("/blogs")



# /blogs - display the string "placeholder to later display a list  of all blogs" with a method named "index"
# /blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
# /blogs/create - redirect to the "/blogs" route with a method called "create"
# /blogs/<number> - display the string "placeholder to display blog number: {{number}}" with a method named "show"
# /blogs/<number>/edit - display the string "placeholder to edit blog {{number}}" with a method named "edit"
# /blogs/<number>/delete - redirect to the "/blogs" route with a method called "destroy"