from django.http import HttpResponse, HttpRequest
from django.contrib.admin import ModelAdmin, action
from django.db.models.query import QuerySet
from .users.models import User
from .mileage.models import Mileage


@action(description="Export selected objects as CSV")
def export2csv(modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet):
    import csv

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{modeladmin.model._meta.model_name}s.csv"'},
    )

    writer = csv.writer(response)
    replacements = {'team_id': 'team_id_name'}
    fields = [replacements.get(f.name, f.name) for f in modeladmin.model._meta.fields if f.name not in ['password', 'is_superuser', 'is_staff', 'is_active']]

    writer.writerow(fields)
    if modeladmin.model == User:
        queryset = queryset.filter(has_consent=True)
    elif modeladmin.model == Mileage:
        queryset = queryset.filter(user__has_consent=True)
    writer.writerows(queryset.values_list(*fields))
    return response
