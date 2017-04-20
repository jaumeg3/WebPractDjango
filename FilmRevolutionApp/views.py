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
    return render_to_response('base.html')


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
        return context


class MovieCreate(CreateView):
    model = Movie
    template_name = 'movies/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)


class SerieDetail(DetailView):
    model = Serie
    template_name = 'series/serie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SerieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = SerieReview.RATING_CHOICES
        return context


class SerieCreate(CreateView):
    model = Serie
    template_name = 'series/form.html'
    form_class = SerieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SerieCreate, self).form_valid(form)


class DirectorDetail(DetailView):
    model = Director
    template_name = 'directors/form.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        return context


class ActorDetail(DetailView):
    model = Actor
    template_name = 'actors/form.html'

    def get_context_data(self, **kwargs):
        context = super(ActorDetail, self).get_context_data(**kwargs)
        return context


class ProductionDetail(DetailView):
    model = Production
    template_name = 'production/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductionDetail, self).get_context_data(**kwargs)
        return context


class PlatformDetail(DetailView):
    model = Platform
    template_name = 'platform/form.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        return context


def reviewM(request, pk):
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
    serie = get_object_or_404(Serie, pk=pk)
    review = SerieReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        serie=serie)
    review.save()
    return HttpResponseRedirect(reverse('FilmRevolutionApp:serie_detail',
                                        args=(serie.id,)))
