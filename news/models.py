# from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.urls import reverse
# from django.utils.text import slugify
# from django.core.validators import MinLengthValidator
# from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError
# from django.conf import settings
# from django.utils import timezone
# from django.contrib.postgres.indexes import GinIndex
# from django.contrib.postgres.search import SearchVectorField
# from ckeditor.fields import RichTextField
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill
# from mptt.models import MPTTModel, TreeForeignKey
# import uuid
# import os


# def article_image_path(instance, filename):
#     """Generate path for article images"""
#     ext = filename.split('.')[-1]
#     filename = f"{uuid.uuid4()}.{ext}"
#     return os.path.join('article_images', timezone.now().strftime('%Y/%m'), filename)


# def journalist_profile_path(instance, filename):
#     """Generate path for journalist profile pictures"""
#     ext = filename.split('.')[-1]
#     filename = f"{uuid.uuid4()}.{ext}"
#     return os.path.join('journalist_profiles', filename)


# class CustomUserManager(UserManager):
#     """Custom user manager with additional methods"""
    
#     def get_journalists(self):
#         return self.filter(groups__name='Journalists', is_active=True)
    
#     def get_editors(self):
#         return self.filter(groups__name='Editors', is_active=True)


# class User(AbstractUser):
#     """Custom user model extending AbstractUser"""
    
#     objects = CustomUserManager()
    
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
#     twitter_handle = models.CharField(max_length=100, blank=True)
#     facebook_url = models.URLField(blank=True)
#     linkedin_url = models.URLField(blank=True)
#     is_verified = models.BooleanField(default=False)
    
#     class Meta:
#         indexes = [
#             models.Index(fields=['username']),
#             models.Index(fields=['email']),
#         ]
    
#     def get_full_name(self):
#         return super().get_full_name() or self.username


# class Category(MPTTModel):
#     """Hierarchical category model using MPTT"""
    
#     name = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=100, unique=True, blank=True)
#     description = models.TextField(blank=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     is_active = models.BooleanField(default=True)
#     featured_image = models.ImageField(upload_to='category_images/', blank=True, null=True)
#     meta_title = models.CharField(max_length=100, blank=True)
#     meta_description = models.CharField(max_length=200, blank=True)
    
#     class MPTTMeta:
#         order_insertion_by = ['name']
    
#     class Meta:
#         verbose_name = _('category')
#         verbose_name_plural = _('categories')
#         indexes = [
#             models.Index(fields=['slug']),
#             GinIndex(fields=['name']),  # GIN index for faster text search
#         ]
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
    
#     def clean(self):
#         if self.parent and self.parent == self:
#             raise ValidationError(_("A category cannot be its own parent."))
    
#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse('category_detail', kwargs={'slug': self.slug})


# class Tag(models.Model):
#     """Tag model with enhanced features"""
    
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(max_length=50, unique=True, blank=True)
#     description = models.TextField(blank=True)
#     featured_image = models.ImageField(upload_to='tag_images/', blank=True, null=True)
#     is_featured = models.BooleanField(default=False)
    
#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['slug']),
#             GinIndex(fields=['name']),
#         ]
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse('tag_detail', kwargs={'slug': self.slug})


# class Journalist(models.Model):
#     """Extended journalist profile model"""
    
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='journalist_profile'
#     )
#     bio = RichTextField(blank=True)
#     profile_picture = ProcessedImageField(
#         upload_to=journalist_profile_path,
#         processors=[ResizeToFill(400, 400)],
#         format='JPEG',
#         options={'quality': 90},
#         blank=True,
#         null=True
#     )
#     twitter_handle = models.CharField(max_length=100, blank=True)
#     linkedin_url = models.URLField(blank=True)
#     is_active = models.BooleanField(default=True)
#     expertise = models.CharField(max_length=200, blank=True)
#     joined_date = models.DateField(auto_now_add=True)
#     awards = models.TextField(blank=True)
#     seo_title = models.CharField(max_length=100, blank=True)
#     seo_description = models.CharField(max_length=200, blank=True)
    
#     class Meta:
#         ordering = ['user__last_name', 'user__first_name']
#         indexes = [
#             models.Index(fields=['is_active']),
#         ]
    
#     def __str__(self):
#         return self.user.get_full_name() or self.user.username
    
#     def get_absolute_url(self):
#         return reverse('journalist_detail', kwargs={'pk': self.pk})


# class Article(models.Model):
#     """Enhanced article model with advanced features"""
    
#     STATUS_CHOICES = [
#         ('draft', _('Draft')),
#         ('review', _('Under Review')),
#         ('published', _('Published')),
#         ('archived', _('Archived')),
#     ]
    
#     CONTENT_TYPE_CHOICES = [
#         ('article', _('Standard Article')),
#         ('news', _('News Report')),
#         ('interview', _('Interview')),
#         ('opinion', _('Opinion Piece')),
#         ('feature', _('Feature Story')),
#     ]
    
#     title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
#     slug = models.SlugField(max_length=200, unique=True, blank=True)
#     content = RichTextField()
#     excerpt = models.TextField(max_length=500, blank=True)
#     search_vector = SearchVectorField(null=True, blank=True)  # For full-text search
    
#     # Relationships
#     author = models.ForeignKey(
#         Journalist,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='articles'
#     )
#     contributors = models.ManyToManyField(
#         Journalist,
#         related_name='contributed_articles',
#         blank=True
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='articles'
#     )
#     tags = models.ManyToManyField(
#         Tag,
#         related_name='articles',
#         blank=True
#     )
#     related_articles = models.ManyToManyField(
#         'self',
#         blank=True,
#         symmetrical=False
#     )
    
#     # Media
#     featured_image = ProcessedImageField(
#         upload_to=article_image_path,
#         processors=[ResizeToFill(1200, 630)],
#         format='JPEG',
#         options={'quality': 85},
#         blank=True,
#         null=True
#     )
#     featured_image_caption = models.CharField(max_length=200, blank=True)
#     video_url = models.URLField(blank=True, null=True)
#     audio_url = models.URLField(blank=True, null=True)
    
#     # Metadata
#     status = models.CharField(
#         max_length=10,
#         choices=STATUS_CHOICES,
#         default='draft'
#     )
#     content_type = models.CharField(
#         max_length=10,
#         choices=CONTENT_TYPE_CHOICES,
#         default='article'
#     )
#     is_breaking = models.BooleanField(default=False)
#     is_trending = models.BooleanField(default=False)
#     is_featured = models.BooleanField(default=False)
#     is_sponsored = models.BooleanField(default=False)
#     allow_comments = models.BooleanField(default=True)
    
#     # Statistics
#     views = models.PositiveIntegerField(default=0)
#     shares = models.PositiveIntegerField(default=0)
#     reading_time = models.PositiveSmallIntegerField(
#         default=5,
#         help_text=_('Estimated reading time in minutes')
#     )
    
#     # SEO
#     meta_title = models.CharField(max_length=100, blank=True)
#     meta_description = models.CharField(max_length=200, blank=True)
#     canonical_url = models.URLField(blank=True)
    
#     # Dates
#     published_at = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-published_at', '-created_at']
#         indexes = [
#             models.Index(fields=['slug']),
#             models.Index(fields=['status', 'published_at']),
#             models.Index(fields=['is_breaking', 'is_trending', 'is_featured']),
#             models.Index(fields=['content_type']),
#             GinIndex(fields=['search_vector']),
#         ]
#         permissions = [
#             ('can_publish', 'Can publish articles'),
#             ('can_feature', 'Can feature articles'),
#             ('can_mark_breaking', 'Can mark articles as breaking news'),
#         ]
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
            
#             # Ensure slug is unique
#             if Article.objects.filter(slug=self.slug).exists():
#                 self.slug = f"{self.slug}-{uuid.uuid4().hex[:4]}"
        
#         # Set published_at if status changes to published
#         if self.status == 'published' and not self.published_at:
#             self.published_at = timezone.now()
        
#         super().save(*args, **kwargs)
    
#     def get_absolute_url(self):
#         return reverse('article_detail', kwargs={'slug': self.slug})
    
#     def __str__(self):
#         return self.title
    
#     @property
#     def is_published(self):
#         return self.status == 'published' and self.published_at <= timezone.now()
    
#     def increment_views(self):
#         self.views += 1
#         self.save(update_fields=['views'])


# class Comment(models.Model):
#     """Enhanced comment system with threading and moderation"""
    
#     article = models.ForeignKey(
#         Article,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='news_comments'
#     )
#     content = models.TextField(validators=[MinLengthValidator(10)])
#     parent = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name='replies'
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_approved = models.BooleanField(default=False)
#     is_flagged = models.BooleanField(default=False)
#     ip_address = models.GenericIPAddressField(blank=True, null=True)
#     user_agent = models.CharField(max_length=200, blank=True)
    
#     class Meta:
#         ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['article', 'created_at']),
#             models.Index(fields=['is_approved', 'is_flagged']),
#         ]
#         permissions = [
#             ('can_moderate', 'Can moderate comments'),
#         ]
    
#     def __str__(self):
#         return f"Comment by {self.author} on {self.article}"
    
#     def clean(self):
#         if self.parent and self.parent.article != self.article:
#             raise ValidationError(_("Reply must be for the same article."))
    
#     def get_depth(self):
#         """Get the nesting depth of the comment"""
#         depth = 0
#         parent = self.parent
#         while parent is not None:
#             depth += 1
#             parent = parent.parent
#             if depth > 5:  # Prevent infinite loops
#                 break
#         return depth


# class Contact(models.Model):
#     """Enhanced contact form submission model"""
    
#     PRIORITY_CHOICES = [
#         ('low', _('Low')),
#         ('medium', _('Medium')),
#         ('high', _('High')),
#     ]
    
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     priority = models.CharField(
#         max_length=10,
#         choices=PRIORITY_CHOICES,
#         default='medium'
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_resolved = models.BooleanField(default=False)
#     resolved_at = models.DateTimeField(blank=True, null=True)
#     resolved_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='resolved_contacts'
#     )
#     ip_address = models.GenericIPAddressField(blank=True, null=True)
    
#     class Meta:
#         ordering = ['-created_at']
#         indexes = [
#             models.Index(fields=['is_resolved', 'priority']),
#         ]
    
#     def __str__(self):
#         return f"Contact from {self.name} - {self.subject}"
    
#     def mark_resolved(self, user):
#         self.is_resolved = True
#         self.resolved_at = timezone.now()
#         self.resolved_by = user
#         self.save()


# class Media(models.Model):
#     """Enhanced media model supporting various file types"""
    
#     MEDIA_TYPE_CHOICES = [
#         ('image', _('Image')),
#         ('video', _('Video')),
#         ('audio', _('Audio')),
#         ('document', _('Document')),
#     ]
    
#     article = models.ForeignKey(
#         Article,
#         on_delete=models.CASCADE,
#         related_name='media'
#     )
#     file = models.FileField(upload_to='article_media/%Y/%m/')
#     media_type = models.CharField(
#         max_length=20,
#         choices=MEDIA_TYPE_CHOICES
#     )
#     caption = models.CharField(max_length=200, blank=True)
#     credit = models.CharField(max_length=100, blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     is_featured = models.BooleanField(default=False)
#     alt_text = models.CharField(max_length=200, blank=True)
    
#     class Meta:
#         ordering = ['-is_featured', 'uploaded_at']
#         verbose_name_plural = _('Media')
    
#     def __str__(self):
#         return f"{self.get_media_type_display()} for {self.article}"
    
#     def clean(self):
#         # Basic validation for file types
#         if self.file:
#             ext = os.path.splitext(self.file.name)[1].lower()
#             if self.media_type == 'image' and ext not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
#                 raise ValidationError(_("Invalid image file format."))
#             elif self.media_type == 'video' and ext not in ['.mp4', '.mov', '.avi', '.webm']:
#                 raise ValidationError(_("Invalid video file format."))
#             elif self.media_type == 'audio' and ext not in ['.mp3', '.wav', '.ogg']:
#                 raise ValidationError(_("Invalid audio file format."))


# class NewsletterSubscriber(models.Model):
#     """Model for newsletter subscribers"""
    
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100, blank=True)
#     is_active = models.BooleanField(default=True)
#     subscribed_at = models.DateTimeField(auto_now_add=True)
#     unsubscribed_at = models.DateTimeField(blank=True, null=True)
#     confirmation_token = models.CharField(max_length=64, blank=True)
#     is_confirmed = models.BooleanField(default=False)
#     preferences = models.JSONField(default=dict)  # For storing subscription preferences
    
#     class Meta:
#         indexes = [
#             models.Index(fields=['email']),
#             models.Index(fields=['is_active']),
#         ]
    
#     def __str__(self):
#         return self.email
    
#     def unsubscribe(self):
#         self.is_active = False
#         self.unsubscribed_at = timezone.now()
#         self.save()


# class ArticleView(models.Model):
#     """Model to track article views in detail"""
    
#     article = models.ForeignKey(
#         Article,
#         on_delete=models.CASCADE,
#         related_name='view_records'
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True
#     )
#     ip_address = models.GenericIPAddressField()
#     user_agent = models.CharField(max_length=200, blank=True)
#     referrer = models.URLField(blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     session_key = models.CharField(max_length=40, blank=True)
    
#     class Meta:
#         indexes = [
#             models.Index(fields=['article', 'timestamp']),
#             models.Index(fields=['ip_address', 'timestamp']),
#         ]
#         unique_together = [('article', 'ip_address', 'session_key')]
    
#     def __str__(self):
#         return f"View of {self.article} at {self.timestamp}"


# class Rating(models.Model):
#     """Article rating system"""
    
#     article = models.ForeignKey(
#         Article,
#         on_delete=models.CASCADE,
#         related_name='ratings'
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='article_ratings'
#     )
#     value = models.PositiveSmallIntegerField(
#         choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         unique_together = [('article', 'user')]
#         indexes = [
#             models.Index(fields=['article', 'user']),
#         ]
    
#     def __str__(self):
#         return f"{self.value} stars for {self.article} by {self.user}"