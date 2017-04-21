from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import MovieReview, SerieReview, Movie, Serie, Director, Actor, \
    Production, Platform
from forms import MovieForm, SerieForm


# Create your views here.

def mainpage(request):
    '''This function return the view of the mainpage of the application'''
    return render_to_response('base.html')


class MovieDetail(DetailView):
    '''This function return the detail view for a movie instance'''
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
        return context


class MovieCreate(CreateView):
    '''This function return a create view to create a movie instance'''
    model = Movie
    template_name = 'movies/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)


class SerieDetail(DetailView):
    '''This function return the detail view for a serie instance'''
    model = Serie
    template_name = 'series/serie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SerieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = SerieReview.RATING_CHOICES
        return context


class SerieCreate(CreateView):
    '''This function return a create view to create a serie instance'''
    model = Serie
    template_name = 'series/form.html'
    form_class = SerieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SerieCreate, self).form_valid(form)


class DirectorDetail(DetailView):
    '''This function return the detail view for a director instance'''
    model = Director
    template_name = 'directors/form.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        return context


class ActorDetail(DetailView):
    '''This function return the detail view for a actor instance'''
    model = Actor
    template_name = 'actors/form.html'

    def get_context_data(self, **kwargs):
        context = super(ActorDetail, self).get_context_data(**kwargs)
        return context


class ProductionDetail(DetailView):
    '''This function return the detail view for a production instance'''
    model = Production
    template_name = 'production/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductionDetail, self).get_context_data(**kwargs)
        return context


class PlatformDetail(DetailView):
    '''This function return the detail view for a platform instance'''
    model = Platform
    template_name = 'platform/form.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        return context


def reviewM(request, pk):
    '''This function return the detail view for a movie review instance'''
    movie = get_object_or_404(Movie, pk=pk)
    reviews = MovieReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        movie=movie)
    reviews.save()
    return HttpResponseRedirect(reverse('FilmRevolutionApp:movie_detail',
                                        args=(movie.id,)))


def reviewS(request, pk):
    '''This function return the detail view for a serie review instance'''
    serie = get_object_or_404(Serie, pk=pk)
    review = SerieReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        serie=serie)
    review.save()
    return HttpResponseRedirect(reverse('FilmRevolutionApp:serie_detail',
                                        args=(serie.id,)))
