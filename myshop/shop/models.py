from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    """Creates a category class which allows us to manually add categories
    through the Django admin page.
    """
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    """Creates a product class which allows us to manually add products
    through the Django admin page.
    """
    category = models.ForeignKey(Category, 
                                 related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', 
                              blank=True)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),) 

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])