from api.models import HackerRank
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

CONTESTS_URL1 = 'https://www.hackerrank.com/rest/contests/upcoming?limit=100'
CONTESTS_URL2 = 'https://www.hackerrank.com/rest/contests/college?limit=100'
 
class HackerRankService(SiteService):

    def extract_contests(self,data1,data2):
        data1 = data1['models']
        for contest in data1:
            contest["type"]="Regular"

        data2 = data2['models']
        for contest in data2:
            contest["type"]="College"    

        data= data1+data2
        sorted(data, key=lambda d: d['epoch_starttime']) 
        return(data)

    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=HackerRankService().extract_contest_info(contest)
            if contest_info is not None:
                data=HackerRank(name=contest_info["name"],
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

        contest_info['end_time']=contest['get_endtimeiso'].replace("T"," ").replace("Z",":000000")
        if datetime.now() > datetime.strptime(contest_info['end_time'], UTC_FORMAT):
            return None
        
        contest_info["name"] = contest['name']
        contest_info["url"] = f"https://hackerrank.com/contests/{contest['slug']}"
        contest_info["type"] = contest["type"]

       

        # '23-03-24T03:30:00Z'
        dt=contest['get_starttimeiso']
        contest_info['start_time'] = dt.replace("T"," ").replace("Z",":000000")
        contest_info['duration'] = contest['epoch_endtime'] - contest['epoch_starttime']
        contest_info["status"] =HackerRankService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =HackerRankService().in_24_hours(contest_info["start_time"],contest_info["status"])
        
         
        return contest_info      


    def update_contests(self):
        HackerRank.objects.all().delete()
        #1.get the html
        response1=HackerRankService().make_request(CONTESTS_URL1)
        response2=HackerRankService().make_request(CONTESTS_URL2)
        
        htmlContent1=response1.content
        htmlContent2=response2.content
        #html has been parsed
        data1 = HackerRankService().create_data_object(htmlContent1)
        data2 = HackerRankService().create_data_object(htmlContent2)

        contests = HackerRankService().extract_contests(data1,data2)
        #print(contests)
        HackerRankService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# HackerRankService().update_contests()      