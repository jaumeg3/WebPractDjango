from django.forms import ModelForm

from models import Movie, Serie, Director, Actor, Production, Platform


class MovieForm(ModelForm):
    '''Movie Form that exclude user and date atributes from the model'''

    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ('user', 'date')


class SerieForm(ModelForm):
    '''Serie Form that exclude user and date atributes from the model'''

    class Meta:
        model = Serie
        fields = "__all__"
        exclude = ('user', 'date')


class DirectorForm(ModelForm):
    '''Director Form that exclude user, date, movie, serie atributes from the 
    model'''

    class Meta:
        model = Director
        fields = "__all__"
        exclude = ('user', 'date')


class ActorForm(ModelForm):
    '''Actor Form that exclude user, date, movie, serie atributes from the 
    model'''

    class Meta:
        model = Actor
        fields = "__all__"
        exclude = ('user', 'date')


class ProductionForm(ModelForm):
    '''Production Form that exclude user, date, movie atributes from the 
    model'''

    class Meta:
        model = Production
        fields = "__all__"
        exclude = ('user', 'date', 'movie')


class PlatformForm(ModelForm):
    '''Platform Form that exclude user, date, serie atributes from the 
    model'''

    class Meta:
        model = Platform
        fields = "__all__"
        exclude = ('user', 'date', 'serie')
