from api.models import AtCoder
from api.services.site_service import SiteService
from datetime import datetime,timedelta
import pytz
from pytz import timezone
from json import dumps
from bs4 import BeautifulSoup

UTC_FORMAT = "%Y-%m-%d %H:%M:%S:%f"
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR   = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY    = SECONDS_IN_HOUR * 24 

CONTESTS_URL = 'https://atcoder.jp/contests'
class AtCoderService(SiteService):

    def extract_contests(self,data):
        tables = data.findAll(class_="table-default")
        
        if len(tables)==4:
            del tables[1]
            tables.pop()
        elif str(data).find("Upcoming Contests")!=-1: 
            tables.pop(0)
            tables.pop()  
        else:
            tables.pop()
            tables.pop()

        return (tables)#upcoming and present

    def create_contests(self,tables):
        for table in tables: # ek ek table pe aa rhe
            contests=table.find("tbody").findAll("tr")
            for contest in contests:
                contest_info = AtCoderService.extract_contest_info(contest)
                data=AtCoder(name=contest_info["name"],
                              url =contest_info["url"],
                              duration = contest_info["duration"],
                              start_time =contest_info["start_time"],
                               end_time =contest_info["end_time"],
                              status =contest_info["status"],
                              in_24_hours =contest_info["in_24_hours"]


                              )
                data.save()

                
        
           
          
    def extract_contest_info(contest):

        tds=contest.findAll("td")
        a=tds[1].a
        # print(tds)
        link=a.get("href")
        contest_info = {}
        contest_info["name"] = a.text
        contest_info["url"] = f"https://atcoder.jp{link}"

        
        duration=tds[2].text
        hours,minutes=duration.split(":")
        # print(tds[2].text) # sample output   216:00
        # print(hours,minutes)#sample output 216 00
        contest_info["duration"] = int(hours) * SECONDS_IN_HOUR + int(minutes) * SECONDS_IN_MINUTE
        contest_info["rated_range"] = tds[3].text
        
        dt =f"{tds[0].a.time.text} JST"
        start_time=datetime.strptime(dt[:-9], '%Y-%m-%d %H:%M:%S').astimezone(pytz.utc)
        contest_info['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S:%f')


        end_time = start_time + timedelta(seconds=contest_info["duration"])
        contest_info['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S:%f')
        contest_info["status"] =AtCoderService().get_status(contest_info["start_time"])
        contest_info["in_24_hours"] =AtCoderService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
        AtCoder.objects.all().delete()
        #1.get the html
        response=AtCoderService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parse
        soup=BeautifulSoup(htmlContent,'html.parser')
  
        #data = AtCoderService().create_data_object(htmlContent)

        contests = AtCoderService().extract_contests(soup)
        #print(contests)
        AtCoderService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

# AtCoderService().update_contests()      