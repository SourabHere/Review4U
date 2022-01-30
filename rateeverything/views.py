import imp
from django.shortcuts import render
from series.models import seriesrev,myrev
from series.models import contact as Contact
from animes.models import animesrev
from animes.models import myrev as myrevanime
from games.models import gamesrev
from games.models import myrev as myrevgame

def index(request):
    series=seriesrev.objects.all()
    animes=animesrev.objects.all()
    games=gamesrev.objects.all()
    series_count=len(series)
    animes_count=len(animes)
    games_count=len(games)
    rangeseries=range(1,series_count)
    rangeanimes=range(1,animes_count)
    rangegames=range(1,games_count)
    
    # series
    myrevall=myrev.objects.all()
    for i in myrevall:
        for l in series:
            if i.series_name==l.series_name:
                l.rating+=i.rating    

    for ser in series:
        count=1
        for rate in myrevall:
            if ser.series_name==rate.series_name:
                count+=1       
        ser.rating=round(ser.rating/count,1)  
        ser.noOfRev=count 

    #animes
    allrev=myrevanime.objects.all()

    for i in allrev:
        for l in animes:
            if i.anime_name == l.anime_name:
                l.rating += i.rating

    for anime in animes:
        count = 1
        for rate in allrev:
            if anime.anime_name == rate.anime_name:
                count += 1
        anime.rating = round(anime.rating/count,1)
        anime.noOfRev = count
    


    #games
    myreval=myrevgame.objects.all()
    for i in myreval:
        for l in games:
            if i.game_name == l.game_name:
                l.rating += i.rating

    for game in games:
        count = 1
        for rate in myreval:
            if game.game_name == rate.game_name:
                count += 1
        game.rating = round(game.rating/count,1)
        game.noOfRev = count

    # params = {'glist': glist, 'range': range(len(glist))}

    params={"series":series,"animes":animes,"games":games,"rangeS":rangeseries,"rangeA":rangeanimes,"rangeG":rangegames}
    return render(request,"index.html",params)

def contact(request):
    if request.method=="POST":
        print(request)
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        # print(username,email,phone)
        contacts=Contact(name=username,email=email,phone=phone,desc=desc)
        contacts.save()
        sent=True
        return render(request,"contact.html",{'sent':sent})
    return render(request,"contact.html")