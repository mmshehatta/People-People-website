

import django_filters

from .models import Offer


class OfferFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # category = django_filters.CharFilter(lookup_expr='icontains')
    place = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Offer
        fields = '__all__'
        exclude = ['owner','date','image','phone','description']
