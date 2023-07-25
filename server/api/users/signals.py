from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from api.users.models import User
from django.core.mail import EmailMessage

# Comment out until working for production
# @receiver(post_save, sender=User)
# def send_new_user_to_admin(sender, instance, created, **kwargs):
#     if created:
#         email = EmailMessage(
#             'Stride For Education: New User Registered',
#             '{} has registered an account on Stride For Education'.format(instance.first_name + " " + instance.last_name),
#             settings.EMAIL_ADDRESS_FROM,
#             [settings.EMAIL_ADDRESS_FROM],
#         )
#         email.send()
