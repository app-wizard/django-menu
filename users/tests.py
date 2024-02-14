from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.form import UserRegistrationForm

User = get_user_model()

class UserRegistrationFormTest(TestCase):
    """Class for testing the user registration form."""

    def test_form_fields(self):
        """Check if all expected fields are present in the form."""
        form = UserRegistrationForm()
        expected_fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        actual_fields = list(form.fields)
        self.assertSequenceEqual(expected_fields, actual_fields)

    def test_form_valid_data(self):
        """Verify the form is valid with correct data provided."""
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complexpassword',
            'password2': 'complexpassword',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

class UserRegistrationViewTest(TestCase):
    """Class for testing the user registration view."""

    def test_registration_view_status_code(self):
        """Ensure the registration page is accessible."""
        response = self.client.get(reverse('users:registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_form_post(self):
        """Test the registration process through the form submission."""
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complexpassword',
            'password2': 'complexpassword',
        }
        response = self.client.post(reverse('users:registration'), form_data)
        self.assertEqual(response.status_code, 302)  # Assuming redirection after successful registration

class UserLoginViewTest(TestCase):
    """Class for testing the login functionality."""

    def test_login_view_status_code(self):
        """Check that the login page is accessible."""
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        """Verify that a user can log in with valid credentials."""
        User.objects.create_user(username='test12345', password='Ttt55555')
        credentials = {'username': 'test12345', 'password': 'Ttt55555'}
        response = self.client.post(reverse('users:login'), credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

class UserProfileViewTest(TestCase):
    """Class for testing the user profile page."""

    def setUp(self):
        """Create a user for testing the profile page."""
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_view_redirect_if_not_logged_in(self):
        """Verify that an unauthenticated user is redirected to the login page."""
        response = self.client.get(reverse('users:profile'))
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('users:profile')}")

    def test_profile_view_with_logged_in_user(self):
        """Ensure the profile page is accessible to an authenticated user."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser')

class UserLogoutViewTest(TestCase):
    """Class for testing the logout functionality."""

    def test_logout_view(self):
        """Check that a user can successfully log out."""
        self.client.login(username='test12345', password='Ttt55555')
        response = self.client.get(reverse('users:logout'), follow=True)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
