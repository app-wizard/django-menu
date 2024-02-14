from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Categories, Products, Comment
from .form import CommentForm

User = get_user_model()

class CommentFormTest(TestCase):
    """
    Tests for the CommentForm functionality.
    """
    def setUp(self):
        """
        Sets up a user for testing the comment form.
        """
        self.user = User.objects.create_user(username='test123456', password='Ttt55555')

    def test_comment_form_label(self):
        """
        Ensures the CommentForm's body field label is set to an empty string.
        """
        form = CommentForm()
        self.assertEqual(form.fields['body'].label, '')

    def test_comment_form_placeholder(self):
        """
        Verifies the CommentForm's body field placeholder text is correctly set.
        """
        form = CommentForm()
        self.assertEqual(form.fields['body'].widget.attrs['placeholder'], 'Enter your comment here...')

class ProductViewTests(TestCase):
    """
    Tests related to viewing products and submitting comments.
    """
    
    @classmethod
    def setUpTestData(cls):
        """
        Creates shared test data for all test methods in the class.
        """
        cls.category = Categories.objects.create(name='Nigiri Selections', slug='nigiri-selections')
        cls.product = Products.objects.create(name='Tuna Sashimi', slug='tuna-sashimi', category=cls.category)
        cls.user = User.objects.create_user(username='test123456', password='Ttt55555')  # Moved user creation here
        
    def test_product_view_status_code(self):
        """
        Tests that the product detail view returns a 200 status code.
        """
        response = self.client.get(reverse('goods:product', args=['tuna-sashimi']))
        self.assertEqual(response.status_code, 200)

    def test_comment_submission(self):
        """
        Tests that a logged-in user can submit a comment on a product.
        """
        self.client.login(username='test123456', password='Ttt55555')
        response = self.client.post(reverse('goods:product', args=['tuna-sashimi']), {'body': 'New Comment'})
        self.assertContains(response, 'New Comment')

class CommentUpdateDeleteTestCase(TestCase):
    """
    Tests for updating and deleting comments.
    """
    
    def setUp(self):
        """
        Sets up the necessary objects for testing comment update and delete functionality.
        """
        self.user = User.objects.create_user(username='test12345', password='Ttt55555')
        self.category = Categories.objects.create(name='TestCategory', slug='test-category')
        self.product = Products.objects.create(name='TestProduct', slug='test-product', category=self.category)
        self.comment = Comment.objects.create(dish=self.product, body='Original Comment', author=self.user, approved=True)
        self.client.login(username='test12345', password='Ttt55555')

    def test_comment_edit(self):
        """
        Ensures that a comment can be edited successfully by its author.
        """
        url = reverse('goods:comment_edit', kwargs={'product_slug': self.product.slug, 'comment_id': self.comment.id})
        response = self.client.post(url, {'body': 'Updated Comment'})
        self.comment.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.comment.body, 'Updated Comment')

    def test_comment_delete(self):
        """
        Ensures that a comment can be deleted successfully by its author.
        """
        url = reverse('goods:comment_delete', kwargs={'product_slug': self.product.slug, 'comment_id': self.comment.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=self.comment.id)
