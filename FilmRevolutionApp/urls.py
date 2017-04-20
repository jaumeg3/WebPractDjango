from django.conf.urls import url
from django.utils import timezone
from django.views.generic import ListView, UpdateView
from models import Movie, Serie
from forms import MovieForm, SerieForm
from views import MovieCreate, SerieCreate, MovieDetail, SerieDetail, \
    DirectorDetail, ActorDetail, PlatformDetail, ProductionDetail, reviewM, \
    reviewS, mainpage

urlpatterns = [
    # List latest 5 movies: /movies/
    url(r'^$', mainpage, name='home'),
    url(r'^movies/$',
        ListView.as_view(
            queryset=Movie.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_movie_list',
            template_name='movies/movie_list.html'),
        name='movie_list'),
    # List latest 5 series: /series/
    url(r'^series/$',
        ListView.as_view(
            queryset=Serie.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_serie_list',
            template_name='series/serie_list.html'),
        name='serie_list'),
    # Movie details, ex.: /movies/1/
    url(r'^movies/(?P<pk>\d+)/$',
        MovieDetail.as_view(),
        name='movie_detail'),
    # Series details, ex.: /series/1/
    url(r'^series/(?P<pk>\d+)/$',
        SerieDetail.as_view(),
        name='serie_detail'),
    # Actors details, ex.: /actors/1/
    url(r'^actors/(?P<pk>\d+)/$',
        ActorDetail.as_view(),
        name='actor_detail'),
    # Director details, ex.: /directors/1/
    url(r'^directors/(?P<pk>\d+)/$',
        DirectorDetail.as_view(),
        name='director_detail'),
    # Platform details, ex.: /platform/1/
    url(r'^platform/(?P<pk>\d+)/$',
        PlatformDetail.as_view(),
        name='platform_detail'),
    # Production details, ex.: /production/1/
    url(r'^production/(?P<pk>\d+)/$',
        ProductionDetail.as_view(),
        name='production_detail'),
    # Create a movies, /movies/create/
    url(r'^movies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),
    # Create a series, /series/create/
    url(r'^series/create/$',
        SerieCreate.as_view(),
        name='serie_create'),
    # Edit movie details, ex.: /movies/1/edit/
    url(r'^movies/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/movie_detail.html',
            form_class=MovieForm),
        name='movies_edit'),
    # Edit serie details, ex.: /movies/1/edit/
    url(r'^series/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Serie,
            template_name='series/serie_detail.html',
            form_class=SerieForm),
        name='series_edit'),
    # Create a movie review, ex.: /movie/1/reviews/create/
    url(r'^movies/(?P<pk>\d+)/reviews/create/$',
        reviewM,
        name='review_movie_create'),
    # Create a serie review, ex.: /series/1/reviews/create/
    url(r'^series/(?P<pk>\d+)/reviews/create/$',
        reviewS,
        name='review_serie_create'),
]
