from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


# Create your models here.

class Movie(models.Model):
    title = models.TextField()
    budget = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField()
    country = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:movie_detail',
                       kwargs={'pk': self.pk})


class Serie(models.Model):
    title = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField()
    numberSeasons = models.IntegerField()
    numberChapters = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:serie_detail',
                       kwargs={'pk': self.pk})


class Actor(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    birthday = models.TextField()
    deathday = models.TextField()
    gender = models.TextField()
    place = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pkm': self.movie.pk, 'pks': self.serie.pk,
                               'pk': self.pk})


class Director(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    birthday = models.TextField()
    deathday = models.TextField()
    gender = models.TextField()
    place = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:director_detail',
                       kwargs={'pkm': self.movie.pk, 'pks': self.serie.pk,
                               'pk': self.pk})


class Platform(models.Model):
    name = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:platform_detail',
                       kwargs={'pks': self.serie.pk, 'pk': self.pk})


class Production(models.Model):
    name = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pkm': self.movie.pk, 'pk': self.pk})


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)',
                                              blank=False,
                                              default=3,
                                              choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class MovieReview(Review):
    movie = models.ForeignKey(Movie)


class SerieReview(Review):
    movie = models.ForeignKey(Serie)
