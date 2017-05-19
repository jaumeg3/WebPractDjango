from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from rest_framework import serializers


# Create your models here.

class Movie(models.Model):
    '''Atributes of Movie '''
    title = models.TextField()
    budget = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField()
    country = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:movie_detail',
                       kwargs={'pk': self.pk})


class Serie(models.Model):
    '''Atributes of Serie '''
    title = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField()
    numberSeasons = models.IntegerField()
    numberChapters = models.IntegerField()
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:serie_detail',
                       kwargs={'pk': self.pk})


class Actor(models.Model):
    '''Atributes of Actor '''
    name = models.TextField()
    age = models.IntegerField()
    birthday = models.TextField()
    deathday = models.TextField(blank=True, null=True)
    gender = models.TextField()
    place = models.TextField()
    serie = models.ForeignKey(Serie, blank=True, null=True,
                              related_name="ActorS")
    movie = models.ForeignKey(Movie, blank=True, null=True,
                              related_name="ActorM")

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pkm': self.movie.pk, 'pks': self.serie.pk,
                               'pk': self.pk})


class Director(models.Model):
    '''Atributes of Director '''
    name = models.TextField()
    age = models.IntegerField()
    birthday = models.TextField()
    deathday = models.TextField(blank=True)
    gender = models.TextField()
    place = models.TextField()
    serie = models.ForeignKey(Serie, blank=True, null=True,
                              related_name="DirectorS")
    movie = models.ForeignKey(Movie, blank=True, null=True,
                              related_name="DirectorM")

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:director_detail',
                       kwargs={'pkm': self.movie.pk, 'pks': self.serie.pk,
                               'pk': self.pk})


class Review(models.Model):
    '''Atributes of Review '''
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


class Platform(models.Model):
    '''Atributes of Platform '''
    name = models.TextField()
    url = models.URLField()
    serie = models.ForeignKey(Serie, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:platform_detail',
                       kwargs={'pks': self.serie.pk, 'pk': self.pk})


class Production(models.Model):
    '''Atributes of Production '''
    name = models.TextField()
    url = models.URLField()
    movie = models.ForeignKey(Movie, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pkm': self.movie.pk, 'pk': self.pk})


class MovieReview(Review):
    '''Review about Movie '''
    movie = models.ForeignKey(Movie)


class SerieReview(Review):
    '''Review of Serie '''
    serie = models.ForeignKey(Serie)
