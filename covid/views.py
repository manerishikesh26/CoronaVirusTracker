from django.shortcuts import render
import requests
import ssl
from .models import *
import json
from django.core.serializers.json import DjangoJSONEncoder
import pandas as pd
import re



def savedata(request):
    #get data from api for all
    url_all = "https://corona.lmao.ninja/all"
    response = requests.get(url_all, verify=ssl.CERT_NONE)
    data_all = response.json()
    all_covid.objects.all().delete()
    all_covid(
        Cases_all=data_all["cases"],
        Deaths=data_all["deaths"],
        Recovered=data_all["recovered"]
    ).save()

    #get data from api for countries
    url = "https://corona.lmao.ninja/countries"
    response = requests.get(url, verify=ssl.CERT_NONE)
    data = response.json()
    print("data :- ", type(data))
    covid19_tb.objects.all().delete()
    for i in data:
        #print("i :- ", i)
        covid19_tb(
            Country=i["country"],
            total_cases=i["cases"],
            today_cases=i["todayCases"],
            total_deaths=i["deaths"],
            today_deaths=i["todayDeaths"],
            recovered=i["recovered"],
            active=i["active"],
            critical=i["critical"]
        ).save()


    #fetchdata
    data_obj = covid19_tb.objects.all().values('Country', 'total_cases', 'today_cases', 'total_deaths', 'today_deaths',
                                               'recovered', 'active', 'critical')

    print("type data_obj :- ", type(data_obj))
    json.dumps(list(data_obj), cls=DjangoJSONEncoder)
    print(type(data_obj))

    df = pd.DataFrame(data_obj)#leo
    #df = df.rename(columns={'total_cases': 'Total Cases'}, )
    df.fillna(0, inplace=True)
    df = df.to_html()
    df1 = re.sub(r'<table border="1"', r'<table', df)
    print(type(df1))

    data_obj_all = all_covid.objects.all().values('Cases_all', 'Deaths', 'Recovered')
    #json.dumps(list(data_obj_all), cls=DjangoJSONEncoder)


    return render(request, 'covid/index.html', {'html_table': df1, 'queryset':data_obj_all})


