import operator

from behave import *
from django.db.models import Q

use_step_matcher("parse")


@when(u'I register movie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(
            context.get_url('FilmRevolutionApp:create_movie'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for restaurant')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in
              context.table.headings]
    from FilmRevolutionApp.models import Movie
    movie = Movie.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(movie)


@then(u'There are {count:n} restaurants')
def step_impl(context, count):
    from FilmRevolutionApp.models import Movie
    assert count == Movie.objects.count()
