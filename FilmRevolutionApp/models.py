from datetime import date

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Platform(models.Model):
    """Atributes of Platform"""
    name = models.TextField()
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    url = models.URLField()
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:platform_detail',
                       kwargs={'pk': self.pk})


class Production(models.Model):
    """Atributes of Production"""
    name = models.TextField()
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    url = models.URLField()
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pk': self.pk})


class Actor(models.Model):
    """Atributes of Actor"""
    name = models.TextField()
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    age = models.IntegerField(validators=[MaxValueValidator(120),
                                          MinValueValidator(1)])
    birthday = models.DateField()
    deathday = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    city = models.TextField(default="")
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:actor_detail',
                       kwargs={'pk': self.pk})


class Director(models.Model):
    """Atributes of Director"""
    name = models.TextField()
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    age = models.IntegerField(validators=[MaxValueValidator(120),
                                          MinValueValidator(1)])
    birthday = models.DateField()
    deathday = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    city = models.TextField(default="")
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:director_detail',
                       kwargs={'pk': self.pk})


class Movie(models.Model):
    """Atributes of Movie"""
    title = models.TextField()
    budget = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField(validators=[MaxValueValidator(100),
                                                 MinValueValidator(1)])
    country = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)
    productor = models.ForeignKey(Production, null=True)
    director = models.ForeignKey(Director, null=True)
    actor = models.ForeignKey(Actor, null=True)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:movie_detail',
                       kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.moviereview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in
                             self.moviereview_set.all()])
            return ratingSum / reviewCount


class Serie(models.Model):
    """Atributes of Serie"""
    title = models.TextField()
    genere = models.TextField()
    url = models.URLField()
    popularity = models.IntegerField(validators=[MaxValueValidator(100),
                                                 MinValueValidator(1)])
    numberSeasons = models.IntegerField(validators=[MinValueValidator(1)])
    numberChapters = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to="FilmRevolutionApp",
                              blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)
    platform = models.ForeignKey(Platform, null=True)
    director = models.ForeignKey(Director, null=True)
    actor = models.ForeignKey(Actor, null=True)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('FilmRevolutionApp:serie_detail',
                       kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.seriereview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in
                             self.seriereview_set.all()])
            return ratingSum / reviewCount


class Review(models.Model):
    """Atributes of Review"""
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
    """Review about Movie"""
    movie = models.ForeignKey(Movie)


class SerieReview(Review):
    """Review of Serie"""
    serie = models.ForeignKey(Serie)
