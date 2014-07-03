from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from signups.views import MyView, HomePageView, ArticleCounterRedirectView, ArticleDetailView, PublisherList, \
    PublisherDetail, BookList, PublisherBookList, ContactView, authentification, create_permission, authenticate_login, \
    register, user_login, user_logout, restricted, user_permissions, some_view, some_view_group_required, TodoList, \
    TodoDetail, TodoCreate, TodoUpdate, TodoDelete, TestBase


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank_you$', 'signups.views.thank_you', name='thank_you'),
    url(r'^about_as$', 'signups.views.about_as', name='about_as'),

    url(r'^test_forms$', 'signups.views.test_forms', name='test_forms'),
    url(r'^Form$', 'signups.views.Form', name='Form'),

    url(r'^bootstrap$', 'signups.views.bootstrap', name='bootstrap'),
    url(r'^angularjs$', 'signups.views.angularjs', name='angularjs'),
    url(r'^nouveau_contact$', 'signups.views.nouveau_contact', name='nouveau_contact'),

    url(r'^voir_contacts$', 'signups.views.voir_contacts', name='voir_contacts'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^multiselect$', 'signups.views.multiselect', name='multiselect'),



    url(r'^myview/(?P<id_test>[0-9]+)/$', MyView.as_view(), name='myview'),
    url(r'^homepageview/(?P<pk>[0-9]+)/$', HomePageView.as_view(template_name = "home.html"), name='homepageview'),
    url(r'^articlecounterredirectview/(?P<pk>[0-9]+)/$', ArticleCounterRedirectView.as_view(), name='articlecounterredirectview'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),


    url(r'^publishers/$', PublisherList.as_view()),

    url(r'^publisher_detail/(?P<pk>[0-9]+)/$', PublisherDetail.as_view()),
    url(r'^book_list/$', BookList.as_view()),


    (r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    (r'^contact_view/$', ContactView.as_view()),
    (r'^thanks/$', ContactView.as_view()),



    url(r'^authentification/([\w-]+)/([\w-]+)$', authentification , name='authentification'),
    url(r'^create_permission/$', create_permission , name='create_permission'),
    url(r'^authenticate_login/$', authenticate_login , name='authenticate_login'),




    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^restricted/$', restricted, name='restricted'),

    url(r'^user_permissions/$', user_permissions, name='user_permissions'),
    url(r'^some_view/$', some_view, name='some_view'),
    url(r'^some_view_group_required/$', some_view_group_required, name='some_view_group_required'),

    #*****************************************
    url(r'^Todo_list/$', TodoList.as_view(), name='todo_list'),

    url(r'^testbase/$', TestBase.as_view(), name='testbase'),

    url(r'^Todo(?P<pk>\d+)$', TodoDetail.as_view(), name='todo_detail'),
    url(r'^New/$', TodoCreate.as_view(), name='todo_create'),
    url(r'^Todo(?P<pk>\d+)/Update$', TodoUpdate.as_view(), name='todo_update'),
    url(r'^Todo(?P<pk>\d+)/Delete$', TodoDelete.as_view(), name='todo_delete'),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('signups.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


