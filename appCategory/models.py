from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(("Category"), max_length=50,null=True)
    slug=models.SlugField(("Category Slug"),blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Subcategory(models.Model):
    title = models.CharField(("Alt Category"), max_length=50,null=True)
    slug=models.SlugField(("Slug Alt Category"),blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    