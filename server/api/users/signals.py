from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from api.users.models import User
from django.core.mail import EmailMessage


@receiver(post_save, sender=User)
def send_new_user_to_admin(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            'A User has registered with CSF',
            '{} has registered with CSF'.format(instance.first_name + " " + instance.last_name),
            settings.EMAIL_ADDRESS_FROM,
            [settings.EMAIL_ADDRESS_FROM],
        )
        email.send()
