from django.conf.urls import include, url
from django.contrib import admin
from address.views import test_html,myaddress,test_html1,contact,thanks,address,home

urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'address.views.hello_world', name='helloworld'),
    url(r'^test/',test_html,name="testhello"),
    url(r'^test1/', test_html1, name="testhello"),
    url(r'^address/',myaddress,name="myaddress"),
    url(r'^ContactForm/',contact,name="contact"),
    url(r'^AddressForm/',address,name="address"),
    url(r'^thanks/',thanks,name='thanks'),
    url(r'^$',home,name='home'),
]
