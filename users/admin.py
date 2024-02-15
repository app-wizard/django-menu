from django.contrib import admin
from users.models import User

# Register User model with the admin site
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Display these fields in the list view of the admin site
    list_display = ["username", "first_name", "last_name", "email",]
    # Enable searching by these fields in the admin site
    search_fields = ["username", "first_name", "last_name", "email",]
