from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(_("age"), null=True)  # this field is added to default User model
    
    @classmethod
    def user_created(cls, sender, user, request, **kwargs):
        from mycustomUserApp.forms import MyRegistrationForm
        form = MyRegistrationForm(request.POST)
        user.age = form.data.get('age', None)
        user.save()
        pass

from registration.signals import user_registered
user_registered.connect(CustomUser.user_created)
