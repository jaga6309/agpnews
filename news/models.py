from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.search import SearchVectorField
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)
    featured_image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='tag_images/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', _('Draft')),
        ('review', _('Under Review')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    ]
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    content = CKEditor5Field()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='articles',
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    is_breaking = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_sponsored = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    
    views = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveSmallIntegerField(
        default=5,
        help_text=_('Estimated reading time in minutes')
    )
    
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    