from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid="5e578bf37cd97794236c3b3342d9a0a6"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    if (request.method)=='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm
    cityes=City.objects.all()
    all_cityes=[]
    for city in cityes:
        res=requests.get(url.format(city.name)).json()
        city_info={
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }
        all_cityes.append(city_info)
    context={'all_info': all_cityes,'form':form}
    return render(request,'weather/index.html',context)