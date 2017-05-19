from rest_framework import serializers
from models import Movie, Serie, Actor, Director, Platform, Production


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
                  'place')


class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    ''' For the API '''
    class Meta:
        model = Director
        fields = ('name', 'age', 'birthday', 'deathday', 'gender',
                  'place')
