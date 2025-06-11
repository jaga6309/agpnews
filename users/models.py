from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile=models.CharField(max_length=10,null=True, blank=True)
    # USER_TYPE_SUPER_ADMIN = 'Super Admin'
    # USER_TYPE_ADMIN = 'Admin'
    # USER_TYPE_APP = 'App User'
    

    # USER_TYPE_CHOICES = (
    #     (USER_TYPE_SUPER_ADMIN, USER_TYPE_SUPER_ADMIN),
    #     (USER_TYPE_ADMIN, USER_TYPE_ADMIN),
    #     (USER_TYPE_APP, USER_TYPE_APP),
        
    # )

    # usertype = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)