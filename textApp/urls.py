from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.urls import re_path
from .views import ThreadView

app_name = 'textApp'

urlpatterns = [

    url(r'^$', login_required(views.IndexView.as_view()), name='index_textApp'),
    re_path(r"^(?P<username>[\w.@+-]+)", login_required(ThreadView.as_view()), name='chaturl'),

]