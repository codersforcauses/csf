from django.contrib.admin import site
from .models import Event

site.register(Event)
