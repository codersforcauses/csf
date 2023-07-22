from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from api.users.models import User


@receiver(post_save, sender=User)
def send_newUser_to_admin(sender, instance, created, **kwargs):
    if created:
        subject = 'A User has registered with CSF'
        message = '{} has registered with CSF'.format(instance.first_name + " " + instance.last_name)
        email_from = settings.EMAIL_ADDRESS_FROM
        recipient = User.objects.get(is_superuser=True).email
        send_mail(subject, message, email_from, [recipient])
