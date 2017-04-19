from django.forms import ModelForm
from models import Movie, Serie, Director, Actor, Production, Platform


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ('user', 'date')


class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = "__all__"
        exclude = ('user', 'date')


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        exclude = ('user', 'date', 'movie', 'serie')


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"
        exclude = ('user', 'date', 'movie', 'serie')


class ProductionForm(ModelForm):
    class Meta:
        model = Production
        fields = "__all__"
        exclude = ('user', 'date', 'movie')


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = "__all__"
        exclude = ('user', 'date', 'serie')
