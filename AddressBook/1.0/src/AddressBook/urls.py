from django.conf.urls import include, url
from django.contrib import admin
#from address.views import hello_world
from address.views import test_html,address_html,contact
from address.views import thanks,address,myhome,aboutus
from newtest_app.views import newtest_html
from settings import dev
from address.api import AddressResource

# creating a address resource

address_resource = AddressResource()

# url patterns for the project

urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'address.views.myhome', name='home'),
    # url(r'^test_html',test_html,name="thtml"),
    url(r'^address_html',address_html,name='details'),
    # url(r'^newtest_html', newtest_html, name='newtest_html'),
    url(r'^contacts',contact,name="contact"),
    url(r'^thanks',thanks,name="thanks"),
    url(r'^address_Form',address,name="Aforms"),
    url(r'^about',aboutus,name="about"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api/', include(address_resource.urls)),
]

if dev.DEBUG:
    import debug_toolbar
    # urlpatterns += patterns('',
    # url(r'^__debug__/', include(debug_toolbar.urls)),
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls))
)

