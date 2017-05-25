from django.conf.urls import url, include
from django.utils import timezone
from django.views.generic import ListView, UpdateView
from models import Movie, Serie, Actor, Director, Production, Platform
from forms import MovieForm, SerieForm, ActorForm, DirectorForm
from views import MovieCreate, SerieCreate, MovieDetail, SerieDetail, \
    DirectorDetail, ActorDetail, PlatformDetail, ProductionDetail, reviewM, \
    reviewS, mainpage, deleteM, deleteS, MovieDetailAPI, MovieListAPI, \
    SerieDetailAPI, SerieListAPI, SerieReviewListAPI, SerieReviewDetailAPI, \
    MovieReviewDetailAPI, MovieReviewListAPI
from rest_framework.urlpatterns import format_suffix_patterns

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
    url(r'^actors/$',
        ListView.as_view(
            queryset=Actor.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_actor_list',
            template_name='actors/actor_list.html'),
        name='actor_list'),
    url(r'^actors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Actor,
            template_name='actors/form.html',
            form_class=ActorForm,),
        name='actor_edit'),
    # Director details, ex.: /directors/1/
    url(r'^directors/(?P<pk>\d+)/$',
        DirectorDetail.as_view(),
        name='director_detail'),
    url(r'^directors/$',
        ListView.as_view(
            queryset=Director.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_director_list',
            template_name='directors/director_list.html'),
        name='director_list'),
    url(r'^directors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Director,
            template_name='directors/form.html',
            form_class=DirectorForm,),
        name='director_edit'),
    # Platform details, ex.: /platform/1/
    url(r'^platform/(?P<pk>\d+)/$',
        PlatformDetail.as_view(),
        name='platform_detail'),
    url(r'^platform/$',
        ListView.as_view(
            queryset=Platform.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_platform_list',
            template_name='platform/platform_list.html'),
        name='platform_list'),
    # Production details, ex.: /production/1/
    url(r'^production/(?P<pk>\d+)/$',
        ProductionDetail.as_view(),
        name='production_detail'),
    url(r'^production/$',
        ListView.as_view(
            queryset=Production.objects.filter(
                date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_production_list',
            template_name='production/production_list.html'),
        name='production_list'),
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
            template_name='movies/form.html',
            form_class=MovieForm),
        name='movies_edit'),
    # Edit serie details, ex.: /movies/1/edit/
    url(r'^series/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Serie,
            template_name='series/form.html',
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
    url(r'^movies/(?P<pk>\d+)/delete/$',
        deleteM,
        name='movies_delete'),
    url(r'^series/(?P<pk>\d+)/delete/$',
        deleteS,
        name='series_delete'),
    url(r'^api/movies$',
        MovieListAPI.as_view(),
        name='movie-list'),
    url(r'^api/movies/(?P<pk>\d+)/$',
        MovieDetailAPI.as_view(),
        name='movie-detail'),
    url(r'^api/movies/(?P<pk>\d+)/reviews$',
        MovieReviewListAPI.as_view(),
        name='movieReview-list'),
    url(r'^api/movies/reviews/(?P<pk>\d+)/$',
        MovieReviewDetailAPI.as_view(),
        name='movieReview-detail'),
    url(r'^api/series$',
        SerieListAPI.as_view(),
        name='serie-list'),
    url(r'^api/series/(?P<pk>\d+)/$',
        SerieDetailAPI.as_view(),
        name='serie-detail'),
    url(r'^api/series/(?P<pk>\d+)/reviews$',
        SerieReviewListAPI.as_view(),
        name='serieReview-list'),
    url(r'^api/series/reviews/(?P<pk>\d+)/$',
        SerieReviewDetailAPI.as_view(),
        name='serieReview-detail'),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
]

# Format suffixes

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
