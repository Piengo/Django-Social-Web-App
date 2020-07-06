from . import views
from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'home'

urlpatterns = [

    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    path('register/location/', views.LocationView.as_view()),

    url(r'profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileUpdate.as_view()), name='profile-update'),

    url(r'^About/$', views.AboutView.as_view(), name='about'),

]