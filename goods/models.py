from django.db import models
from cloudinary.models import CloudinaryField

from users.models import User


class Categories(models.Model):
    """
    Model representing categories of products.
    """
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Products(models.Model):
    """
    Model representing products.
    """
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField("image", default="placeholder")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        """
        Calculate the selling price considering the discount.
        """
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price


class Comment(models.Model):
    """
    Model representing comments on products.
    """
    dish = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
