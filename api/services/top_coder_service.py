from api.models import TopCoder
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

CONTESTS_URL = 'https://api.topcoder.com/v4/srms/schedule?orderBy=registrationStartTime%20desc&filter=registrationStartTimeAfter%3D2021-03-01T00%3A00%3A00.000%2B0300%26registrationStartTimeBefore%3D2024-04-01T00%3A00%3A00.000%2B0300%26statuses%3DP'
class TopCoderService(SiteService):

    def extract_contests(self,data):
        return data['result']['content']
       



    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=TopCoderService().extract_contest_info(contest)
            if contest_info is not None:
                data=TopCoder(name=contest_info["name"],
                              url =contest_info["url"],
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
        contest_info["end_time"] = contest['codingEndTime'].replace("T"," ").replace(".000Z",":000000")
       
        if datetime.now() > datetime.strptime(contest_info['end_time'], UTC_FORMAT):
            return None
        contest_info["name"] = contest['contestName']
        contest_info["url"] = "https://www.topcoder.com/challenges"
        

        
        contest_info["start_time"] =contest['codingStartTime'].replace("T"," ").replace(".000Z",":000000")
        start_time_dt = datetime.strptime(contest_info["start_time"], '%Y-%m-%d %H:%M:%S:%f')
        end_time_dt = datetime.strptime( contest_info["end_time"], '%Y-%m-%d %H:%M:%S:%f')
        difference = end_time_dt - start_time_dt
        contest_info["duration"] =int(difference.total_seconds())
        contest_info["status"] =TopCoderService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =TopCoderService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
        TopCoder.objects.all().delete()
        #1.get the html
        response=TopCoderService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parsed
        data = TopCoderService().create_data_object(htmlContent)
        # print(data)
        contests = TopCoderService().extract_contests(data)
        # #print(contests)
        TopCoderService().create_contests(contests)
          

# TopCoderService().update_contests()      



