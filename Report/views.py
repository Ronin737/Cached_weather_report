from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.views import View
from django.http import HttpResponse
import requests
import json
from .utils import serialize

'''Class-based views for urls'''

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class ReportAPI(View):
    '''API view for displaying data'''

    def get(self,request,data,nocache=0):
        jsondict={'data':''}
        if(data=='ping'):
            jsondict['data']='pong'
        else:
            station_code=data
            if(cache.get(station_code) and nocache!=1):  #checking for key in cache
                jsondict['data']=cache.get(station_code)
            else:
                station_data=requests.get(f'https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station_code}.TXT')
                jsondict['data']=serialize(station_data.text)
                if(nocache==1): 
                    cache.clear() #refreshing cache
                cache.set(station_code,jsondict['data'])
        
        jsondict=json.dumps(jsondict) #converting data to JSON

        return HttpResponse(jsondict)


class HomeViewAPI(View):

    def get(self,request):
        return HttpResponse('Enter station code in URL to get METAR report')
        


        


