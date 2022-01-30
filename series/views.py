from django.shortcuts import render
# from django.http import HttpResponse
from .models import seriesrev,myrev
from.models import contact as Contact

# Create your views here.
def index(request):
    # serieslist=[]
    slist=seriesrev.objects.all()
    myrevall=myrev.objects.all()

    # allseries={}

    # for j in slist:
        # series_name=j.series_name
        # allseries[series_name]=j.rating

    for i in myrevall:
        # series_name=i.series_name
        for l in slist:
            if i.series_name==l.series_name:
                l.rating+=i.rating    
        # if i.series_name in allseries:
            # allseries[series_name]+=i.rating
        # else:
            # allseries[series_name]=i.rating

    for series in slist:
        # print("in",series.series_name)
        count=1
        for rate in myrevall:
            # print("in",rate.series_name,count)
            if series.series_name==rate.series_name:
                count+=1
                # print("count upgraded")
        # print(series.series_name,series.rating,count)        
        series.rating=round(series.rating/count,1)  
        series.noOfRev=count  
        # allseries[series.series_name]=allseries[series.series_name]/count    
    # print(allseries)        

    params={'slist':slist,'range':range(len(slist))}

    return render(request,"series/index.html",params)
    # return HttpResponse("hello")

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
        return render(request,"series/Contact.html",{'sent':sent})
    return render(request,"series/Contact.html")

def addrev(request):
    if request.method=="POST":
        print(request)
        email=request.POST.get('email','')
        series_name=request.POST.get('series_name','')
        rel_date=request.POST.get('rel_date','')
        desc=request.POST.get('desc','')
        img=request.FILES.get('img','')
        rating=request.POST.get('rating','')
        # print(email,series_name,rel_date,desc,img,rating)
        series=seriesrev(email=email,series_name=series_name,release_date=rel_date,desc=desc,rating=rating,series_img=img)
        series.save()
        id=series.series_id
        posted=True
        return render(request,"series/AddRev.html",{"posted":posted})      
    return render(request,"series/AddRev.html")    
def about(request):
    return render(request,"series/about.html")   
def myreview(request,series_id):
    Series=seriesrev.objects.filter(series_id=series_id)
    if request.method=="POST":
        print(request)
        email=request.POST.get('email','')
        name=request.POST.get('name','')
        rating=request.POST.get('rating','')
        series_name=request.POST.get('series_name','')
        # print(email,name,rating,series_name,username)
        mrev=myrev(email=email,username=name,rating=rating,series_name=series_name)
        mrev.save()
        posted=True
        return render(request,"series/myreview.html",{'series':Series[0],'posted':posted})
    return render(request,"series/myreview.html",{'series':Series[0]})     

def moredetail(request,series_id):
    Series=seriesrev.objects.filter(series_id=series_id)
    myrevdistinct=myrev.objects.filter(series_name=Series[0].series_name)
    rate=Series[0].rating
    for i in myrevdistinct:
        rate+=i.rating
    rate=rate/(len(myrevdistinct)+1)
    rate=round(rate,1)
    return render(request,"series/moredetail.html",{'series':Series[0],'rating':rate,'count':(len(myrevdistinct)+1)})