from django.http import HttpResponse, HttpRequest
from django.contrib.admin import ModelAdmin, action
from django.db.models.query import QuerySet


@action(description="Export selected objects as CSV")
def export2csv(modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet):
    import csv

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="events.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(f.name for f in modeladmin.model._meta.fields)
    writer.writerows(queryset.values_list())
    return response
