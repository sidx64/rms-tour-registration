from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from registration.registrationapi.views import create_profile, email_confirmation

urlpatterns = {
    url(r'^$', views.landing),
    url(r'^api/register/$', create_profile),
    url(r'^api/verify/' r'(?P<code>.*)/$', email_confirmation),

}


urlpatterns = format_suffix_patterns(urlpatterns)