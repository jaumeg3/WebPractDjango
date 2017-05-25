from django.test import TestCase
from django.contrib.auth.models import User
from models import MovieReview, SerieReview, Movie, Serie


# Create your tests here.
class ReviewTestCase(TestCase):
    def setUp(self):
        trendy = Movie.objects.create(title="Trendy	Movie", popularity=50)
        top = Serie.objects.create(title = "Top Serie",popularity = 45)
        user1 = User.objects.create(user="user1")
        user2 = User.objects.create(user="user2")
        user3 = User.objects.create(user="user3")
        MovieReview.objects.create(rating=3, comment="Average...",\
                                   movie=trendy, user=user1)
        SerieReview.objects.create(rating=3, comment="Average...", \
                                   serie=top, user=user1)
        MovieReview.objects.create(rating=5, comment="Excellent!",\
                                   movie=trendy, user=user2)
        SerieReview.objects.create(rating=5, comment="Excellent!", \
                                   serie=top, user=user2)
        MovieReview.objects.create(rating=1, comment="Really bad!",\
                                   movie=trendy, user=user3)
        SerieReview.objects.create(rating=1, comment="Really bad!", \
                                   serie=top, user=user3)
        Movie.objects.create(title="Unknown	Movie", popularity=41)
        Serie.objects.create(title="Unknown	Serie", popularity=33)

    def test_average_3reviews(self):
        """The	average	review	for	a	movie and serie	with 3 reviews is \
        properly computed"""
        movie = Movie.objects.get(title="Trendy Restaurant")
        serie = Serie.objects.get(title="Top Serie")
        self.assertEqual(movie.averageRating(), 3)
        self.assertEqual(serie.averageRating(), 3)

    def test_average_no_review(self):
        """The average	review	for	a Movie	without	reviews	is	0"""
        movie = Movie.objects.get(title="Unknown Restaurant")
        serie = Serie.objects.get(title="Unknown Serie")
        self.assertEqual(movie.averageRating(), 0)
        self.assertEqual(serie.averageRating(), 0)