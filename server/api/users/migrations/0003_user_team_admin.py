# Generated by Django 4.2.2 on 2023-07-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_id_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team_admin',
            field=models.BooleanField(default=False),
        ),
    ]
