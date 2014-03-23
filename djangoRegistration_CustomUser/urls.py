from django.conf.urls import patterns, include, url


from django.contrib import admin
from mycustomUserApp.forms import MyRegistrationForm
from registration.backends.default.views import RegistrationView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoRegistration_CustomUser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=MyRegistrationForm),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
