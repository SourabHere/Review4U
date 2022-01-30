from django.shortcuts import render
from django.http import HttpResponse
from .models import gamesrev, myrev
from.models import contact as Contact
# Create your views here.


def index(request):
    glist = gamesrev.objects.all()
    myreval = myrev.objects.all()

    for i in myreval:
        for l in glist:
            if i.game_name == l.game_name:
                l.rating += i.rating

    for game in glist:
        count = 1
        for rate in myreval:
            if game.game_name == rate.game_name:
                count += 1
                # print("count upgraded")
        game.rating = round(game.rating/count,1)
        game.noOfRev = count

    params = {'glist': glist, 'range': range(len(glist))}

    # return HttpResponse("hello")
    return render(request, "games/index.html",params)


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get("username", '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        contacts = Contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
        sent = True
        return render(request, "games/contact.html", {"sent": sent})

    return render(request, "games/contact.html")


def myreview(request,games_id):
    Games=gamesrev.objects.filter(games_id=games_id)
    if request.method=="POST":
        print(request)
        email=request.POST.get('email','')
        name=request.POST.get('name','')
        rating=request.POST.get('rating','')
        game_name=request.POST.get('game_name','')
        print(email,name,rating,game_name,name)
        mrev=myrev(email=email,username=name,rating=rating,game_name=game_name)
        mrev.save()
        posted=True
        return render(request,"games/myrev.html",{'games':Games[0],'posted':posted})
    return render(request, "games/myrev.html",{'games':Games[0]})


def about(request):
    return render(request, "games/aboutgame.html")


def addrev(request):
    if request.method == "POST":
        print(request)
        email = request.POST.get('email', '')
        game_name = request.POST.get('game_name', '')
        rel_date = request.POST.get('rel_date', '')
        desc = request.POST.get('desc', '')
        game_img = request.FILES.get('img', '')
        rating = request.POST.get('rating', '')

        # print(email,game_name,rel_date,desc,game_img,rating)
        games = gamesrev(email=email, game_name=game_name,release_date=rel_date, desc=desc, game_img=game_img, rating=rating)
        games.save()
        id = games.games_id
        posted = True
        return render(request, "games/Addrev.html", {"posted": posted})

    return render(request, "games/Addrev.html")

def detail(request,games_id):
    Games=gamesrev.objects.filter(games_id=games_id)
    myrevdistinct=myrev.objects.filter(game_name=Games[0].game_name)
    rate=Games[0].rating
    for i in myrevdistinct:
        rate+=i.rating
    rate=rate/(len(myrevdistinct)+1)
    rate=round(rate,1)
    return render(request,"games/moredetail.html",{"games":Games[0],'rating':rate,'count':(len(myrevdistinct)+1)})