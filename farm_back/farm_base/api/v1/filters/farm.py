import django_filters
from django_filters import FilterSet, filters

from farm_base.api.v1.filters.fields import NumberInFilter
from farm_base.models import Farm, Owner


class FarmFilter(FilterSet):
    ids = NumberInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Farm
        #Added the owner's id, owner's document, municipality and state into the filters of Farm.
        fields = ['ids', 'name', 'municipality', 'state', 'owner__id', 'owner__document']