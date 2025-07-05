import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    date = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Event
        fields = ['location', 'date']
