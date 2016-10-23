from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    def __unicode__(self):
        return unicode("%s" % self.user.username)

    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=15, blank=True)
    # Payment related information
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    cc_last4 = models.CharField(max_length=4, blank=True)
    cc_brand = models.CharField(max_length=99, blank=True)
    cc_expiration_date = models.DateField(null=True, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
