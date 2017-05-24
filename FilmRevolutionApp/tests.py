from django.test import TestCase
from django.contrib.auth.models import User
from models import MovieReview, Movie


# Create your tests here.
class MovieReviewTestCase(TestCase):
    def setUp(self):
        trendy = Movie.objects.create(title="Trendy	Movie", popularity=50)
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        MovieReview.objects.create(rating=3, comment="Average...",\
                                   movie=trendy, user=user1)
        MovieReview.objects.create(rating=5, comment="Excellent!",\
                                   movie=trendy, user=user2)
        MovieReview.objects.create(rating=1, comment="Really bad!",\
                                   movie=trendy, user=user3)
        Movie.objects.create(title="Unknown	Movie", popularity=41)

    def test_average_3reviews(self):
        """The	average	review	for	a	movie	with	3	reviews	is	properly	computed"""
        movie = Movie.objects.get(title="Trendy Restaurant")
        self.assertEqual(movie.averageRating(), 3)

