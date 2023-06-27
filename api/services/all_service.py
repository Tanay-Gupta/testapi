from api.models import *


class AllServices:

  def copy_data(self):
    models = [
      Leetcode,
      CodeChef,
      Codeforces,
      HackerRank,
      HackerEarth,
      CSAcademy,
      AtCoder,
      TopCoder,
      CodeForcesGym,
  ]
    """Copies data from the given models to the `AllContests` model."""
    AllContests.objects.all().delete()
    all_contests = AllContests.objects.order_by('start_time')
    for model in models:
      for contest in model.objects.all():
        contest_info = {
            'name': contest.name,
            'url': contest.url,
            'duration': contest.duration,
            'start_time': contest.start_time,
            'end_time': contest.end_time,
            'status': contest.status,
            'in_24_hours': contest.in_24_hours,
        }
        all_contests.update_or_create(**contest_info)

 

