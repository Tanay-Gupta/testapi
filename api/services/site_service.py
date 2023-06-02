import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time
from pytz import timezone
from api.models import Leetcode

UTC_FORMAT = '%Y-%m-%d %H:%M:%S:%f'
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR   = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY    = SECONDS_IN_HOUR * 24 
USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


class SiteService:

    def make_request(self,siteUrl):
        return(requests.get(siteUrl,headers=USER_AGENT))

    def create_data_object(self,htmlContent):
        #2.parsing the html
        soup=BeautifulSoup(htmlContent,'html.parser')
        # convert into JSON:
        #y  = json.dumps(soup.text)# json to str
        y=json.loads(soup.text)#str to json
        return(y)
        # print(type(y))
        # for i in y["future_contests"]:
        #     print(i)
    

    def get_status (self,start_time):
        s = datetime.strptime(start_time, UTC_FORMAT) #converting a datetime string into a specific datetime format
        if(s< datetime.utcnow()):
            return ("CODING")
        else:
            return ("BEFORE")


    def in_24_hours(self,start_time,status):
        s = datetime.strptime(start_time, UTC_FORMAT) #converting a datetime string into a specific datetime format
        if status=="CODING":
            return "False"
        else:
            diff=(s - datetime.utcnow()).total_seconds() / SECONDS_IN_HOUR
            if diff <= 24 and diff > 0:
                return "True"
            else:    
                return "False"  

    # def get_status(self,start_time):
    #     return(start_time < Time.now.in_time_zone('UTC') if "CODING" else "BEFORE")


