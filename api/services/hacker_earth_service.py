from site_service import SiteService
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
                print(contest_info)
            #add to table    
    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['title']
        contest_info["url"] = contest['url']
        contest_info["type_"] = contest['challenge_type']
        # contest_info["duration"] = contest['duration']

        # _________________________________Items to be fixed (START)__________________________________________

        #BHUT SARE TIME STAMP AVAILABLE HAIN UPAR LINK PE JA KE USKO PRETIFY KAR DEKH LO
        
        #     start_time = Time.zone.parse(contest['start_timestamp']).in_time_zone('UTC')
    # end_time = Time.zone.parse(contest['end_timestamp']).in_time_zone('UTC')
    # contest_info[:duration] = end_time - start_time

    # return nil if Time.now > end_time

    # contest_info[:start_time] = start_time.strftime UTC_FORMAT
    # contest_info[:end_time] = end_time.strftime UTC_FORMAT


        # _________________________________Items to be fixed (END)__________________________________________
       



        # contest_info["status"] =LeetCodeService().get_status(contest_info["start_time"])
        # contest_info["in_24_hours"] =LeetCodeService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
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

HackerEarthService().update_contests()      