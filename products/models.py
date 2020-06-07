from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='media/images/category/%Y/%m/%d/', default='No image')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Product(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/images/products/%Y/%m/%d/', default='No image')
    category = models.ForeignKey(Category, related_name='Category', blank=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='Tag', blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='Country', blank=True, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('product_detail', args=[
            self.slug,
        ])

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True