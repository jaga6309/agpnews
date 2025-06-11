from django.contrib import admin
from .models import *


admin.site.register((Category, Article, Tag))
# Register your models here.
