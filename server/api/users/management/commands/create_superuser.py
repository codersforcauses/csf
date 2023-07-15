from django.core.management.base import BaseCommand
from api.users.models import User


class Command(BaseCommand):
    help = "To create a superuser, enter a username with -u <username> and password with -p <password>."

    def add_arguments(self, parser):
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="The username for the user to be created.",
        )
        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="The password for the user to be created.",
        )
        parser.add_argument(
            "-e", "--email", type=str, help="The email for the user to be created."
        )

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        extra_fields = {}
        if kwargs["email"]:
            extra_fields = {"email": kwargs["email"]}

        if username and password:
            # Account for already existing
            try:
                User.objects.create_superuser(
                    username=username, password=password, **extra_fields
                )
                print(f"Successfully created superuser with username: {username}")
            except ValueError:
                print(f"User already exist: {username}")
        else:
            print(self.help)
