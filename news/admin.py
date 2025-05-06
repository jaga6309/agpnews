from django.contrib import admin
from .models import *

admin.site.register((Category, Article))
# Register your models here.
