from tastypie.resources import ModelResource

from .models import Address


class AddressResource(ModelResource):
    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'


 #https://django-tastypie.readthedocs.io/en/latest/tutorial.html#configuration