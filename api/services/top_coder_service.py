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

CONTESTS_URL = 'https://clients6.google.com/calendar/v3/calendars/appirio.com_bhga3musitat85mhdrng9035jg@group.calendar.google.com/events?calendarId=appirio.com_bhga3musitat85mhdrng9035jg%40group.calendar.google.com&timeMin=2019-01-01T00%3A00%3A00-04%3A00&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs'
class TopCoderService(SiteService):

    def extract_contests(self,data):
        data = data['items']
        #data.select! { |element| not element['start'].nil? and not element['start']['dateTime'].nil? }
        #print(data)
        newdata=[]
        for element in data:
            if "start" in element.keys() and "dateTime" in element['start'].keys() :
                newdata.append(element)

       # data.sort_by! { |element| Time.parse(element['start']['dateTime']).in_time_zone('UTC') }
        return newdata



    def create_contests(self,contests):
        for contest in contests:
            #print(contest)
            contest_info=TopCoderService().extract_contest_info(contest)
            if contest_info is not None:
                print(contest_info)
            #add to table    
    def extract_contest_info(self,contest):

        contest_info = {}
        contest_info["name"] = contest['summary']
        contest_info["url"] = "https://www.topcoder.com/challenges"
        

        # _________________________________Items to be fixed (START)__________________________________________


        #bhai ye alag alag timezone return kar raha ek baar iska json dekh lena
    #      start_time = Time.parse(contest['start']['dateTime']).in_time_zone('UTC')
    # end_time = Time.parse(contest['end']['dateTime']).in_time_zone('UTC')

    # return nil if Time.now > end_time

    # contest_info["duration"]  = end_time - start_time

    #    contest_info[:start_time] = start_time.strftime UTC_FORMAT
    # contest_info[:end_time] = end_time.strftime UTC_FORMAT
        # _________________________________Items to be fixed (END)__________________________________________
       



        # contest_info["status"] =TopCoderService().get_status(contest_info["start_time"])
        # contest_info["in_24_hours"] =TopCoderService().in_24_hours(contest_info["start_time"],contest_info["status"])
        return contest_info      


    def update_contests(self):
        #1.get the html
        response=TopCoderService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parsed
        data = TopCoderService().create_data_object(htmlContent)

        contests = TopCoderService().extract_contests(data)
        #print(contests)
        TopCoderService().create_contests(contests)
        # for i in contests:
        #     print(i)
        #print(contests)    

TopCoderService().update_contests()      



