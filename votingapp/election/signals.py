from election.models import CreateElection
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import UserProfile


@receiver(post_save, sender=CreateElection)
def change_profile(sender, instance, created, **kwargs):
    pos=UserProfile.objects.all()

    for p in pos:
        p.voted=False
        p.save()