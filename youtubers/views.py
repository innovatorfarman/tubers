from ast import keyword
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from .models import Youtuber

#Views
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtuber.html', data)

def youtuber_details(request, id):
    youtuber_details = get_object_or_404(Youtuber, pk=id)
    data = {
        'yd':youtuber_details
    }
    return render(request, 'youtubers/youtuber_details.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')  
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera', flat = True).distinct()
     
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        tubers = tubers.filter(description__icontains = keyword)
    
    if 'city' in request.GET:
        city = request.GET['city']
        tubers = Youtuber.objects.filter(city__iexact = city)
    
    if 'category' in request.GET:
        category = request.GET['category']
        tubers = Youtuber.objects.filter(category__iexact = category)
    if 'camera' in request.GET:
        camera = request.GET['camera']
        tubers = Youtuber.objects.filter(camera__iexact = camera)
    

    data = {
        'tubers':tubers,
        'city_search':city_search,
        'category_search': category_search,
        'camera_search': camera_search,
    }
        
    return render(request, 'youtubers/search.html', data)