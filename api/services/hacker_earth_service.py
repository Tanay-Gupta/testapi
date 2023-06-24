from api.models import HackerEarth
from api.services.site_service import SiteService
from datetime import datetime
import time
from pytz import timezone
from json import dumps
import dateutil


UTC_FORMAT = "%Y-%m-%d %H:%M:%S:%f"
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR   = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY    = SECONDS_IN_HOUR * 24 

CONTESTS_URL = 'https://www.hackerearth.com/chrome-extension/events'

class HackerEarthService(SiteService):

    def extract_contests(self,data):
        return( data['response'])

    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=HackerEarthService().extract_contest_info(contest)
            if contest_info is not None:
                data=HackerEarth(name=contest_info["name"],
                              url =contest_info["url"],
                              type= contest_info["type"],
                              duration = contest_info["duration"],
                              start_time =contest_info["start_time"],
                               end_time =contest_info["end_time"],
                              status =contest_info["status"],
                              in_24_hours =contest_info["in_24_hours"]



                              )
                data.save()
            #add to table    
    def extract_contest_info(self,contest):

        contest_info = {}

        contest_info['end_time']=contest['end_utc_tz'].replace("+00:00",':00000')
        if datetime.now() > datetime.strptime(contest_info['end_time'], UTC_FORMAT):
            return None 
        contest_info["name"] = contest['title']
        contest_info["url"] = contest['url']
        contest_info["type"] = contest['challenge_type']

      
        contest_info['start_time'] = contest['start_utc_tz'].replace("+00:00",':00000')
        start_time_dt = datetime.strptime(contest_info["start_time"], '%Y-%m-%d %H:%M:%S:%f')
        end_time_dt = datetime.strptime( contest_info["end_time"], '%Y-%m-%d %H:%M:%S:%f')
        difference = end_time_dt - start_time_dt
        contest_info["duration"] =int(difference.total_seconds())

        contest_info["status"] =HackerEarthService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =HackerEarthService().in_24_hours(contest_info["start_time"],contest_info["status"])
        # '2023-07-07 12:30:00+00:00'
        # 2014-07-07 15:38:00:00000
        
        return contest_info      


    def update_contests(self):
        HackerEarth.objects.all().delete()
        #1.get the html
        response=HackerEarthService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parsed
        data = HackerEarthService().create_data_object(htmlContent)

        contests = HackerEarthService().extract_contests(data)
        #print(contests)
        HackerEarthService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# HackerEarthService().update_contests()      