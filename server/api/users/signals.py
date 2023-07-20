from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def send_newUser_to_admin(sender, instance, created, **kwargs):
    if created:
        subject = 'A User has registered with CSF'
        message = 'User {} has registered'.format(instance.username)
        email_from = settings.EMAIL_ADDRESS_FROM
        recipient_list = settings.EMAIL_ADDRESS_USER
        send_mail(subject, message, email_from, recipient_list)
