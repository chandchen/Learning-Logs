from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login website
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # Logout website
    url(r'^logout/$', views.logout_view, name='logout'),
    # Sign Up website
    url(r'^register/$', views.register, name='register'),
]