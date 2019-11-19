from .models import Paste
import django_filters
from django import forms
class UserFilter(django_filters.FilterSet):
    ageofg = django_filters.NumberFilter(name='ageof', lookup_expr='Age__lte')
    ageofl = django_filters.NumberFilter(name='ageof', lookup_expr='Age__gte')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Paste.Strain,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Paste
        fields = ['Strain', 'Age', ]
