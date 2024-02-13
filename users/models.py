from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

#Create your models here.
class User(AbstractUser):
    # image = models.ImageField(upload_to="users_images", blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering: list[str] = ["id"]

    def __str__(self):
        return f"{self.username}"
