from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
def home(request):
    cdata=category.objects.all().order_by('-id')[0:8]
    ndata=news.objects.all().order_by('-id')[0:8]
    x=notification.objects.all().order_by('-id')[0:3]
    sdata=slider.objects.all().order_by('-id')[0:2]

    #ndata=news.objects.filter(id=1)

    return render(request,'user/index.html',{'a':cdata,'b':ndata,'c':x,'slider':sdata})

def aboutus(request):
    return render(request,'user/aboutus.html')


def mynews(request):
    mycity=city.objects.all().order_by('-id')
    a=request.GET.get('msg')
    cid=request.GET.get('cid')
    sdata=request.GET.get('search')
    print(sdata)

    if a is not None:
        ndata = news.objects.filter(ncategory=a)
    elif cid is not None:
        ndata=news.objects.filter(ncity=cid)
    elif sdata is not None:
        x=news.objects.filter(Q(nhead__icontaines=sdata) |Q (ndes__icontaines=sdata))
        if len(x)>0:
            ndata=x;
        else:
            return HttpResponse("<script>alert('Data not Found....');window.location.href='/user/news'</script>")
    else:
        ndata=news.objects.all().order_by('-id')

    cdata=category.objects.all().order_by('-id')
    return render(request,'user/news.html',{"cat":cdata,"n":ndata,'city':mycity})

def contactus(request):
    status=False
    if request.method=='POST':
        name=request.POST.get('name')
        mobno=request.POST.get('mobno')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        res=contact(name=name, mobno=mobno, email=email,msg=msg)
        res.save()
        status=True
    return render(request,'user/contactus.html',context={"s":status})

def video(request):
    cid = request.GET.get('cid')
    cdata = category.objects.all().order_by('-id')
    if cid is not None:
        vdata= videonews.objects.filter(vcategory=cid)
    else:
        vdata = videonews.objects.all().order_by('-id')

    return render(request,'user/video.html',{"a":vdata,'b':cdata})

def viewmore(request):
    a=request.GET.get('msg')

    ndata=news.objects.filter(id=a)


    return render(request,'user/viewmore.html',{'data':ndata})
