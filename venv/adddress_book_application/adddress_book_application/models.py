from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=30, unique=False, blank=True)
    last_name = models.TextField(max_length=30, unique=False, blank=True)
    phone_number = models.TextField(max_length=13, unique=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, blank=True)
    street_address = models.TextField(mex_length=254, unique=False, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def del_user(request, username):
    try:
        u = User.objects.get(username = username)
        u.delete()
        message.success(request, "Contact deleted")
    except User.DoesNoteExist:
        message.error(request, "Contact does not exist")
        return render(request, 'home.html')
    except Exception as e:
        return render(request, 'home.html', {'err': e.message})

    return render(request, 'home.html')

def get_current_contacts():
    active_session = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_session:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
        return User.objects.filter(id_in=user_id_list)