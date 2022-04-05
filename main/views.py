from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseNotFound
from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def eventregister(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        venue = request.POST.get('venue')
        eventdata = events_DB(name=name,desc=desc,venue=venue)
        eventdata.save()
        message = "Data Saved Succesfully"
        return render(request,"event_register.html",{'message':message})
    return render(request,"event_register.html")

def showallevent(request):
    eventdata = events_DB.objects.all()
    return render(request,"event_show.html",{'eventdata':eventdata})

def showoneevent(request,id):
    oneeventdata = events_DB.objects.get(id=id)
    return render(request,"one_event_show.html",{'oneeventdata':oneeventdata})

def deleteevent(request,id):
    oneeventdata = events_DB.objects.get(id=id)
    oneeventdata.delete()
    return redirect('showallevent')
    

