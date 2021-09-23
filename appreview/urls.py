from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    url(r'^$',views.homepage,name="index"),
    url(r'favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    url(r'^accounts/register/',RegistrationView.as_view(success_url='/accounts/login/'),name="register"),
    url(r'^accounts/logout/',LogoutView.as_view(),{'next':'/'}),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^appreview/addproject/',views.addproject,name="addnewproject"),
    url(r'^(\d)/vote/',views.add,name="add"),
    url(r'^profile/(\d)/',views.profile,name="profile"),
    url(r'^profileupdate/(\d)/',views.updateprofile,name='updateprofile'),
    url(r'^appreview/api/$',views.AppList.as_view()),
   
    
]
