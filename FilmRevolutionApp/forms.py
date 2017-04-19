from django.forms import ModelForm
from models import Movie, Serie, Director, Actor, Production, Platform


class MovieForm(ModelForm):
    class Meta:
        model = Movie

    exclude = ('user', 'date',)


class SerieForm(ModelForm):
    class Meta:
        model = Serie

    exclude = ('user', 'date',)


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        exclude = ('user', 'date', 'movie', 'serie',)


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        exclude = ('user', 'date', 'movie', 'serie',)


class ProductionForm(ModelForm):
    class Meta:
        model = Production
        exclude = ('user', 'date', 'movie',)


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        exclude = ('user', 'date', 'serie',)
