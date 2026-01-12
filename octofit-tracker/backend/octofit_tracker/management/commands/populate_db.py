from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create workouts
        workouts = [
            Workout(name='Super Strength', description='Strength training for superheroes', suggested_for='Marvel'),
            Workout(name='Flight Training', description='Flight skills for superheroes', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create activities
        tony = User.objects.get(email='tony@stark.com')
        bruce = User.objects.get(email='bruce@wayne.com')
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=45, date=timezone.now().date())

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
