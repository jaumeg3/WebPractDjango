from django.contrib.auth.models import User
from django.test import TestCase
from models import MovieReview, Movie, SerieReview, Serie


class SerieReviewTestCase(TestCase):
    def setUp(self):
        trendy = Serie.objects.create(title="Trendy Serie", popularity=2,
                                      numberSeasons=6, numberChapters=25)
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        SerieReview.objects.create(rating=3, comment="Average...", serie=trendy
                                   , user=user1)
        SerieReview.objects.create(rating=5, comment="Excellent!", serie=trendy
                                   , user=user2)
        SerieReview.objects.create(rating=1, comment="Really bad!",
                                   serie=trendy, user=user3)
        Serie.objects.create(title="Unknown Serie", popularity=1,
                             numberSeasons=6, numberChapters=25)

    def test_average_3reviews(self):
        """The average review for a restaurant with 3 reviews is properly
        computed"""
        serie = Serie.objects.get(title="Trendy Serie")
        self.assertEqual(serie.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a restaurant without reviews is 0"""
        serie = Serie.objects.get(title="Unknown Serie")
        self.assertEqual(serie.averageRating(), 0)


class MovieReviewTestCase(TestCase):
    def setUp(self):
        trendy = Movie.objects.create(title="Trendy Movie", popularity=2)
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        MovieReview.objects.create(rating=3, comment="Average...", movie=trendy
                                   , user=user1)
        MovieReview.objects.create(rating=5, comment="Excellent!", movie=trendy
                                   , user=user2)
        MovieReview.objects.create(rating=1, comment="Really bad!",
                                   movie=trendy, user=user3)
        Movie.objects.create(title="Unknown Movie", popularity=1)

    def test_average_3reviews(self):
        """The average review for a restaurant with 3 reviews is properly
        computed"""
        movie = Movie.objects.get(title="Trendy Movie")
        self.assertEqual(movie.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a restaurant without reviews is 0"""
        movie = Movie.objects.get(title="Unknown Movie")
        self.assertEqual(movie.averageRating(), 0)

