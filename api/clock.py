# from api.services.all_service import AllServices
from api.services.at_coder_service import AtCoderService
from api.services.code_chef_service import CodeChefService
from api.services.codeforces_gym_service import CodeforcesGymService
from api.services.codeforces_service import CodeforcesService
from api.services.hacker_earth_service import HackerEarthService
from api.services.hacker_rank_service import HackerRankService
from api.services.leet_code_service import LeetCodeService

from django_cron import CronJobBase, Schedule
import random

from api.services.top_coder_service import TopCoderService


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    ALLOW_PARALLEL_RUNS = True

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.my_cron_job2'    # a unique code

    def do(self):
       LeetCodeService().update_contests()
       CodeChefService().update_contests()
       CodeforcesGymService().update_contests()  
       CodeforcesService().update_contests()
       AtCoderService().update_contests()
       HackerRankService().update_contests() 
       TopCoderService().update_contests()      
       HackerEarthService().update_contests()
    #    AllServices().copy_data()






        








# def handler(job):
#     if job == "frequent.2_min":
#         AllService().update_contests()
#     elif job == "frequent.3_min":
#         CodeforcesService().update_contests()
#         CodeforcesGymService().update_contests()
#         TopCoderService().update_contests()
#         AtCoderService().update_contests()
#     elif job == "frequent.5_min":
#         CodeChefService().update_contests()
#         HackerRankService().update_contests()
#         HackerEarthService().update_contests()
#         LeetCodeService().update_contests()
#     elif job == "frequent.7_min":
#         CsAcademyService().update_contests()
#         # KickStartService().update_contests()
#         TophService().update_contests()

# cron.add_job(handler, '*/2 * * * *', 'frequent.2_min')
# cron.add_job(handler, '*/3 * * * *', 'frequent.3_min')
# cron.add_job(handler, '*/5 * * * *', 'frequent.5_min')
# cron.add_job(handler, '*/7 * * * *', 'frequent.7_min')
