from api.models import Leetcode
from api.services.site_service import SiteService
from datetime import datetime
import time
from pytz import timezone

UTC_FORMAT = "%Y-%m-%d %H:%M:%S:%f"

CONTESTS_URL = 'https://leetcode.com/graphql?query={%20allContests%20{%20title%20titleSlug%20startTime%20duration%20__typename%20}%20}'

class LeetCodeService(SiteService):

    def extract_contests(self,data):
        return( data['data']['allContests'])

    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=LeetCodeService().extract_contest_info(contest)
            if contest_info is not None:
                data=Leetcode(name=contest_info["name"],
                              url =contest_info["url"],
                              duration = contest_info["duration"],
                              start_time =contest_info["start_time"],
                               end_time =contest_info["end_time"],
                              status =contest_info["status"],
                              in_24_hours =contest_info["in_24_hours"]


                              )
                data.save()
            #add to table  


    def unixToUtc(self,unixTimeStamp) -> str:
        #time_stamp = 1668306600 (unix time stamp) example
        original_time = datetime.fromtimestamp(unixTimeStamp)
        utc_time = original_time.astimezone(timezone('UTC'))
        start_time = utc_time.strftime(UTC_FORMAT)
        return start_time #returns string


    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['title']
        contest_info["url"] = f"https://leetcode.com/contest/{contest['titleSlug']}"
        contest_info["duration"] = int(contest['duration'])
        contest_info["start_time"] = LeetCodeService().unixToUtc(contest['startTime'])
        contest_info["end_time"] = LeetCodeService().unixToUtc(contest['startTime']+contest_info["duration"])
        if(datetime.utcnow() > datetime.strptime(contest_info["end_time"], UTC_FORMAT)):
            return None
        contest_info["status"] =LeetCodeService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =LeetCodeService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
        Leetcode.objects.all().delete()
        #1.get the html
        response=LeetCodeService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parsed
        data = LeetCodeService().create_data_object(htmlContent)

        contests = LeetCodeService().extract_contests(data)
        #print(contests)
        LeetCodeService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# LeetCodeService().update_contests()      
