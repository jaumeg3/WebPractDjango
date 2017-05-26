from rest_framework import serializers
from models import Movie, Serie, Actor, Director, Platform, Production, \
    MovieReview, SerieReview


class MovieSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Movie
        fields = ('title', 'budget', 'genere', 'url', 'popularity', 'country')


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
                  'city')


class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Director
        fields = ('name', 'age', 'birthday', 'deathday', 'gender',
                  'city')


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
