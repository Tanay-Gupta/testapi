from site_service import SiteService
from datetime import datetime
import time
from bs4 import BeautifulSoup
from pytz import timezone
from json import dumps
import dateutil


UTC_FORMAT = "%Y-%m-%d %H:%M:%S:%f"


CONTESTS_URL = 'https://codingcompetitions.withgoogle.com/kickstart/schedule'
class KickStartService(SiteService):

    def extract_contests(self,data):
        for css in data.find_all('.schedule-row__upcoming'):
            print(css)

    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=KickStartService().extract_contest_info(contest)
            if contest_info is not None:
                print(contest_info)
            #add to table    



    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['title']
        contest_info["url"] = f"https://leetcode.com/contest/{contest['titleSlug']}"
        contest_info["duration"] = int(contest['duration'])

        # _________________________________Items to be fixed (START)__________________________________________
        # _________________________________Items to be fixed (END)__________________________________________
       



        # contest_info["status"] =LeetCodeService().get_status(contest_info["start_time"])
        # contest_info["in_24_hours"] =LeetCodeService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
        #1.get the html
        response=KickStartService().make_request(CONTESTS_URL)

        htmlContent=response.content

        soup=BeautifulSoup(htmlContent,'html.parser')
        print(soup)
        #html has been parsed
        # data = KickStartService().create_data_object(htmlContent)

        #contests = KickStartService().extract_contests(soup)
        #print(contests)
        #KickStartService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

KickStartService().update_contests()      