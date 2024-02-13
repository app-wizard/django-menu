from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering: list[str] = ["id"]

    def __str__(self):
        return f"{self.name}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price
