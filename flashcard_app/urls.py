from django.conf.urls import patterns, include, url

urlpatterns = patterns('flashcard_app.views',
    url(r'^$','list_cards', name='list_cards'),
    url(r'^(?P<pk>\d+)/$','show_card', name='show_card'),
    url(r'^create/$', 'create_card', name='create_card'),
)