from api.models import Leetcode
from api.services.leet_code_service import LeetCodeService
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.my_cron_job'    # a unique code

    def do(self):
        #Leetcode.objects.all().delete()
        LeetCodeService().update_contests()








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
