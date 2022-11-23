from django.shortcuts import render,redirect
from .models import Slider ,Team 
from youtubers.models import Youtuber
from django.contrib import messages
# Create your views here.
def home(request):
    sliders = Slider.objects.all() # querying model/db 
    team = Team.objects.all() #fetch all team members 

    youtubers = Youtuber.objects.all() #fetch all Youtubers
    
    featured_ytubers = Youtuber.objects.filter(is_featured=True)


    data ={

        'sliders' :sliders,
        'team':team,
        'youtubers':youtubers,
         'featured_ytubers':featured_ytubers,
    }


    return render(request,'webpages/home.html',data)
    

def about(request):

    team = Team.objects.all() #fetch all team members 
    data ={

    
        'team':team,
      
    }

    return render(request,'webpages/about.html',data)


def services(request):
    return render(request,'webpages/services.html')


def contact(request):

      
    return render(request,'webpages/contact.html')



