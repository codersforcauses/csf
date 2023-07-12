from typing import TextIO
from django.apps import apps
import csv


def model_data_2_csv(model_name: str, csv_file: TextIO):
    writer = csv.writer(csv_file)
    model = apps.get_model('api', model_name)
    writer.writerow(f.name for f in model._meta.fields)
    writer.writerows(model.objects.all().values_list())
