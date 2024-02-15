from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.form import UserRegistrationForm

User = get_user_model()

class UserRegistrationFormTest(TestCase):
    """Test cases for the user registration form."""

    def test_form_fields(self):
        """Test if all expected fields are present in the form."""
        # Create an instance of the form and check its fields
        form = UserRegistrationForm()
        expected_fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        actual_fields = list(form.fields)
        self.assertSequenceEqual(expected_fields, actual_fields)

    def test_form_valid_data(self):
        """Test the form's validation with correct data."""
        # Create form data with valid input and check if the form is valid
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
    """Test cases for the user registration view."""

    def test_registration_view_status_code(self):
        """Test if the registration page is accessible."""
        # Access the registration page and check its status code
        response = self.client.get(reverse('users:registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_form_post(self):
        """Test the registration process by submitting the registration form."""
        # Submit registration form data and check the redirection status
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
