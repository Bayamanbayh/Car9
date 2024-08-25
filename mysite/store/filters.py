from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt', 'lt'],
            'created_date': ['gt', 'lt'],
            'have': ['exact'],
        }