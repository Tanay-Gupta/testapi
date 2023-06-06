from api.models import CodeChef
from api.services.site_service import SiteService
from datetime import datetime
import time
from pytz import timezone
UTC_FORMAT = "%Y-%m-%d %H:%M:%S:%f"
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR   = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY    = SECONDS_IN_HOUR * 24 


url="https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all"
class CodeChefService(SiteService):


    def extract_contests(self,data):
        # Should practice_contests be added to the list? e.g. ` +data['future_contests']+ data['practice_contests']+data['present_contests'] +`
        return( data['present_contests']+data['future_contests'])

    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            if "contest_end_date_iso" in contest.keys():
                contest_info=CodeChefService().extract_contest_info(contest)
                data=CodeChef(name=contest_info["name"],
                              url =contest_info["url"],
                              duration = contest_info["duration"],
                              start_time =contest_info["start_time"],
                               end_time =contest_info["end_time"],
                              status =contest_info["status"],
                              in_24_hours =contest_info["in_24_hours"]


                              )
                data.save()
            #add to table
    def isoToUtc(self,isoTime) -> str:
        #time_stamp = "2022-11-08T20:00:00+05:30" example
        original_time = datetime.strptime(isoTime, "%Y-%m-%dT%H:%M:%S%z")
        utc_time = original_time.astimezone(timezone('UTC'))
        start_time = utc_time.strftime(UTC_FORMAT)
        return start_time #returns string

    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['contest_name']
        contest_info["url"] = f"https://www.codechef.com/{contest['contest_code']}"
        
        contest_info["start_time"] =CodeChefService().isoToUtc(contest['contest_start_date_iso'])

        if "contest_end_date_iso" in contest.keys():
            contest_info["duration"] = int(contest['contest_duration'])*SECONDS_IN_MINUTE
            contest_info["end_time"]=CodeChefService().isoToUtc(contest['contest_end_date_iso'])
        else: 
            contest_info['end_time'] = CodeChefService().isoToUtc(contest['contest_start_date_iso'] + datetime.timedelta(years=10))
            contest_info['duration'] = contest_info['end_time'] - contest_info['start_time']
 
        contest_info["status"] =CodeChefService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =CodeChefService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info



    def update_contests(self):
        CodeChef.objects.all().delete()
        #1.get the html
        response=CodeChefService().make_request(url)

        htmlContent=response.content
        #html has been parsed
        data = CodeChefService().create_data_object(htmlContent)

        contests = CodeChefService().extract_contests(data)
        #print(contests)
        CodeChefService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# CodeChefService().update_contests()
