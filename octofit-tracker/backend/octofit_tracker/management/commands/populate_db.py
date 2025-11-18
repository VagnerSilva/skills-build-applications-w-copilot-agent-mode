from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-11-18')
        Activity.objects.create(user='Batman', type='cycle', duration=45, date='2025-11-17')
        Activity.objects.create(user='Wonder Woman', type='swim', duration=60, date='2025-11-16')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=250, rank=1)
        Leaderboard.objects.create(team='dc', points=200, rank=2)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m x 5', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
