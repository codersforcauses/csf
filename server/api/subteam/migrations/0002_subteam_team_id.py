# Generated by Django 4.2.2 on 2023-07-02 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('subteam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subteam',
            name='team_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='teamOf', to='team.team'),
        ),
    ]
