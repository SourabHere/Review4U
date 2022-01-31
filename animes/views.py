from platform import release
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import contact,animesrev, myrev
from .models import myrev as Myrev
import operator

# Create your views here.
def index(request):
    alist=animesrev.objects.all()
    allrev=Myrev.objects.all()

    for i in allrev:
        for l in alist:
            if i.anime_name == l.anime_name:
                l.rating += i.rating

    for anime in alist:
        count = 1
        for rate in allrev:
            if anime.anime_name == rate.anime_name:
                count += 1
                # print("count upgraded")
        anime.rating = round(anime.rating/count,1)
        anime.noOfRev = count

    # print(alist)

    params = {'alist': alist, 'range': range(len(alist))}
    # return HttpResponse("hello")
    return render(request,"animes/index.html",params)

def Contact(request):
    alist=animesrev.objects.all()
    if request.method=="POST":
        print(request)
        name=request.POST.get('username','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        phone=request.POST.get('phone','')
        posted=True
        # print(name,email,desc,phone)
        allcontact=contact(name=name,email=email,desc=desc,phone=phone)
        allcontact.save()
        return render(request,"animes/contact.html",{'posted':posted})
    return render(request,"animes/contact.html",{"alist":alist})

def addrev(request):
    alist=animesrev.objects.all()
    if request.method=="POST":
        print(request)
        email=request.POST.get('email','')
        anime_name=request.POST.get('anime_name','')
        release_date=request.POST.get('rel_date','')
        desc=request.POST.get('desc','')
        anime_img=request.FILES.get('img','')
        rating=request.POST.get('rating','')
        posted=True
        # print(email,anime_name,release_date,desc,game_img,rating)

        addedrev=animesrev(email=email,anime_name=anime_name,release_date=release_date,desc=desc,anime_img=anime_img,rating=rating)
        addedrev.save()
        return render(request,"animes/addrev.html",{'posted':posted})
    return render(request,"animes/addrev.html",{"alist":alist})

def myreview(request,anime_id):
    alist=animesrev.objects.all()
    Animes=animesrev.objects.filter(anime_id=anime_id)
    if request.method=="POST":
        print(request)
        email=request.POST.get('email','')
        name=request.POST.get('name','')
        rating=request.POST.get('rating','')
        anime_name=request.POST.get('anime_name','')
        # print(email,name,rating,anime_name,name)
        mrev=Myrev(email=email,username=name,rating=rating,anime_name=anime_name)
        mrev.save()
        posted=True
        return render(request,"animes/myrev.html",{'animes':Animes[0],'posted':posted})
    return render(request,"animes/myrev.html",{'animes':Animes[0],"alist":alist})

def about(request):
    alist=animesrev.objects.all()
    return render(request,"animes/about.html",{"alist":alist})

def moredetail(request,anime_id):
    alist=animesrev.objects.all()
    Animes=animesrev.objects.filter(anime_id=anime_id)
    myrevdist=Myrev.objects.filter(anime_name=Animes[0].anime_name)
    rate=Animes[0].rating
    for i in myrevdist:
        rate+=i.rating
    rate=rate/(len(myrevdist)+1)
    rate=round(rate,1)
    return render(request,"animes/moredetail.html",{'animes':Animes[0],'rating':rate,'count':len(myrevdist)+1,'alist':alist})
