from rest_framework import serializers
from models import Movie, Serie, Actor, Director, Platform, Production, \
    MovieReview, SerieReview


class MovieSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Movie
        fields = ('title', 'budget', 'genere', 'url', 'popularity', 'country')


class MovieReviewSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = MovieReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'movie')


class SerieReviewSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = SerieReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'serie')


class SerieSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Serie
        fields = ('title', 'genere', 'url', 'popularity', 'numberSeasons',
                  'numberChapters')


class ActorSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Actor
        fields = ('name', 'age', 'birthday', 'deathday', 'gender',
                  'place')


class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Director
        fields = ('name', 'age', 'birthday', 'deathday', 'gender',
                  'place')


class PlatformSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Platform
        fields = ('name', 'url')


class ProductionSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Production
        fields = ('name', 'url')
