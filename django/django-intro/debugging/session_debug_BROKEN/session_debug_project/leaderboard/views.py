from django.shortcuts import render, redirect

# Create your views here.
def index(request): 

    return render(request, "index.html")


def leaderBoard(request):

    # if "user_name" not in request.session:
    #     print('redirecting...')
    #     return redirect('/')

    ranks = ["first", "second", "third"]

    for key in ranks:
        if key not in request.session:
            request.session[key] = "Please assign a rank."

    return render(request, "leaderboard.html")

def show(request, rank):

    name = ''
    if rank == 1:
        if request.session['first'] == "Please assign a rank.":
            return redirect('/dashboard')
        else: 
            name = request.session['first']
    elif rank == 2:
        if request.session['second'] == "Please assign a rank.":
            return redirect('/dashboard')
        else:
            name = request.session['second']
    elif rank == 3:
        if request.session['third'] == "Please assign a rank.":
            return redirect('/dashboard')
        else:
            name = request.session['third']

    return render(request, "showFriend.html", {"name": name, "rank": rank})

def enter(request):
    
    if request.method == "POST":
    
        user_name = request.POST["first_name"] + " " + request.POST["last_name"]
        if 'user_name' not in request.session:
            request.session['user_name'] = user_name
        return redirect('/leaderboard')

def changeRanks(request):

    # print(request.POST)
    if 'first' in request.session:
        request.session['first'] = request.POST['first']
        print("**"*20)
    if 'second' in request.session:
        request.session['second'] = request.POST['second']

    if 'third' in request.session:
        request.session['third'] = request.POST['third']
        
    print("**"*20)
    return redirect('/leaderboard')

def logout(request):
    request.session.clear()
    return redirect('/')