# Generated by Django 4.2.2 on 2023-07-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubTeam',
            fields=[
                ('subteam_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
    ]
