from django.test import TestCase
from .models import User

# Create your tests here.


class MyTest(TestCase):
    def setUp(self):
        """
        This method is run before each test
        """
        User.objects.create(
            email="test@user.com",
            username="testuser",
            first_name="Test",
            last_name="User")

    def test_user_count(self):
        """
        Test number of users in the database
        """
        self.assertEqual(User.objects.count(), 1)
