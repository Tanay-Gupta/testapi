from api.models import Codeforces
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


CONTESTS_URL = 'https://codeforces.com/api/contest.list'

class CodeforcesService(SiteService):
    def extract_contests(self,data):
        return( data['result'])


    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            if contest['phase']=="BEFORE" or contest['phase']=="CODING":
                contest_info=CodeforcesService().extract_contest_info(contest)
                data=Codeforces(name=contest_info["name"],
                              url =contest_info["url"],
                              duration = contest_info["duration"],
                              start_time =contest_info["start_time"],
                               end_time =contest_info["end_time"],
                              status =contest_info["status"],
                              in_24_hours =contest_info["in_24_hours"]


                              )
                data.save()

    def unixToUtc(self,unixTimeStamp) -> str:
        #time_stamp = 1668306600 (unix time stamp) example
        original_time = datetime.fromtimestamp(unixTimeStamp)
        utc_time = original_time.astimezone(timezone('UTC'))
        start_time = utc_time.strftime(UTC_FORMAT)
        return start_time #returns string

    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['name']
        contest_info["url"] = f"https://codeforces.com/contestRegistration/{contest['id']}"
        contest_info["duration"] = contest['durationSeconds']
        contest_info["status"] = contest['phase']
        
        if (bool(contest['startTimeSeconds']) == False):
            contest_info["start_time"] = '-'
            contest_info["end_time"] = '-'
            in_24_hours = False
        else:
            contest_info["start_time"] = CodeforcesService().unixToUtc(contest['startTimeSeconds'])
            contest_info["end_time"] = CodeforcesService().unixToUtc(contest['startTimeSeconds']+contest_info["duration"])
            contest_info["in_24_hours"] = CodeforcesService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info



    def update_contests(self):
        Codeforces.objects.all().delete()
        #1.get the html
        response=CodeforcesService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parsed
        data = CodeforcesService().create_data_object(htmlContent)

        contests = CodeforcesService().extract_contests(data)
        #print(contests)
        CodeforcesService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# CodeforcesService().update_contests()    



