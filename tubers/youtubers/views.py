from django.shortcuts import render,get_object_or_404
from .models import Youtuber


# Create your views here.
def youtubers(request):

    youtubers = Youtuber.objects.all()

    data={
     'youtubers':    youtubers
    }
    return render(request,'youtubers/youtubers.html',data)
    
    


def youtuber_details(request,id):
    tuber = get_object_or_404(Youtuber,pk=id)
    

    data={
     'tuber':    tuber
    }
    return render(request,'youtubers/tuberdetail.html',data)

# common search views
def search(request):
    
    tuber = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()

    camera_search = Youtuber.objects.values_list('camera',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
  

  # keyword based search 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            tuber =   tuber.filter(description__icontains=keyword)
   

    # city  based exact search 
    if 'city' in request.GET:
        city = request.GET['city']
        # print("city found ")
        if city:
            tuber =   tuber.filter(city__iexact=city)
   
   # camera  based exact search 
    if 'camera' in request.GET:
        camera = request.GET['camera']
        # print("camera found ")
        if camera:
            tuber =   tuber.filter(camera__iexact=camera)
 # category  based exact search 
    if 'category' in request.GET:
        category = request.GET['category']
        # print("category found ")
        if category:
            tuber =   tuber.filter(category__iexact=category)
   
    data={
     'tuber':    tuber,
     'city_search':  city_search,
     'camera_search':camera_search,
     'category_search':category_search
    }
    return render(request,'youtubers/search.html',data)