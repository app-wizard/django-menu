from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    """
    Custom user model extending AbstractUser to include additional fields.
    """
    # Use CloudinaryField for storing user images
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["id"]  # Corrected the assignment operator to '='

    def __str__(self):
        """
        Return the string representation of the user (username).
        """
        return f"{self.username}"
