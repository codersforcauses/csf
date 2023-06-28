from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = "To create a superuser, enter a username with -u <username> and password with -p <password>."

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='The username for the user to be created.')
        parser.add_argument('-p', '--password', type=str, help='The password for the user to be created.')
        parser.add_argument('-e', '--email', type=str, help='The email for the user to be created.')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        extra_fields = {'email': kwargs['email']} if 'email' in kwargs else {}

        if username and password:
            User.objects.create_superuser(username=username, password=password, **extra_fields)
        
        else:
            print(self.help)