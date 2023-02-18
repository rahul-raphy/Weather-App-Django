from django.shortcuts import render
import requests
import datetime
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kochi'

    appid = ''  #You need to enter your openweathermap API KEY here
    PARAMS = {'q':city,'appid':appid,'units':'metric'}
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    r = requests.get(URL,PARAMS)
    res=r.json()
    description = res["weather"][0]["description"]
    icon = res["weather"][0]["icon"]
    temp = res["main"]["temp"]
    day = datetime.date.today()
    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})

