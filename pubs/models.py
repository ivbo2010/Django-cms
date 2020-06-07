from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils import timezone


class PubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='media/images/pub_category/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Pub(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/images/pub/%Y/%m/%d/', blank=True)
    pub_category = models.ForeignKey(PubCategory, related_name='PubCategory', blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('pub_detail', args=[
            self.slug,
            self.id,
        ])

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
