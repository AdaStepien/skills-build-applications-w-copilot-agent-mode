from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout', suggested_for='Test')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=60, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=10)

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Test Activity')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 10)
