from django.db import models
from . managers import ActiveLinkManager
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Link(models.Model):
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Link"
    target_url =models.URLField(max_length = 200)
    description = models.CharField(max_length = 200)
    identifier = models.SlugField(max_length=20,unique=True, blank=True) 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)  
    created_date = models.DateTimeField(auto_now=True, null=True) 
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()


    def __str__(self):
        return self.target_url
