from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    # URL pattern for user login
    path("login/", views.login, name="login"),
    # URL pattern for user registration
    path("registration/", views.registration, name="registration"),
    # URL pattern for user profile
    path("profile/", views.profile, name="profile"),
    # URL pattern for user logout
    path("logout/", views.logout, name="logout"),
]
