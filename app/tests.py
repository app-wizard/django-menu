from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from . import views 

User = get_user_model()

class URLAccessTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test123456', password='Ttt55555')

    def test_user_page_status_code(self):
        """
        Tests that the user profile page is accessible and returns a 200 status code.
        Ensures that user profile or account page functions correctly.
        """
        self.client.login(username='test123456', password='Ttt55555')
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        """
        Tests that the home page is accessible and returns a 200 status code.
        This ensures the main page loads correctly for users.
        """
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_status_code(self):
        """
        Tests that the catalog page is accessible and returns a 200 status code.
        Verifies that users can access the catalog of goods without issues.
        """
        response = self.client.get(reverse('goods:index', kwargs={'category_slug': 'all'}))
        self.assertEqual(response.status_code, 200)

class ErrorPagesTests(TestCase):
    def setUp(self):
        """
        Setup before running tests. Uses RequestFactory to create requests.
        """
        self.factory = RequestFactory()

    def test_handler404(self):
        """
        Tests the custom 404 error page.
        Checks that the 404 error page returns a 404 status code.
        """
        request = self.factory.get('/nonexistent_url')
        response = views.handler404(request, exception=None)
        self.assertEqual(response.status_code, 404)

    def test_handler500(self):
        """
        Tests the custom 500 error page.
        Ensures that the 500 error page returns a 500 status code.
        """
        request = self.factory.get('/url_causing_server_error')
        response = views.handler500(request)
        self.assertEqual(response.status_code, 500)

    def test_handler403(self):
        """
        Tests the custom 403 error page.
        Verifies that the 403 error page returns a 403 status code.
        """
        request = self.factory.get('/forbidden_url')
        response = views.handler403(request, exception=None)
        self.assertEqual(response.status_code, 403)

    def test_handler405(self):
        """
        Tests the custom 405 error page.
        Checks that the 405 error page returns a 405 status code.
        """
        request = self.factory.post('/url_not_allowing_post')
        response = views.handler405(request, exception=None)
        self.assertEqual(response.status_code, 405)