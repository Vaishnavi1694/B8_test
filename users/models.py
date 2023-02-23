# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import ugettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     mobile_no = models.IntegerField(null = True)
#     address = models.CharField(max_length = 255, default = "")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     mobile_no = models.IntegerField(null = True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)