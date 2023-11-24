from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        # Create a test Parent user
        self.parent_user = User.objects.create(
            first_name='John',
            last_name='Doe',
            address_street='123 Main St',
            address_city='City',
            address_state='State',
            address_zip='12345',
            user_type='Parent',
        )

        # Create a test Child user
        self.child_user = User.objects.create(
            first_name='Jane',
            last_name='Doe',
            user_type='Child',
            parent=self.parent_user,
        )

    def test_parent_user_has_address(self):
        self.assertEqual(self.parent_user.address_street, '123 Main St')
        self.assertEqual(self.parent_user.address_city, 'City')
        self.assertEqual(self.parent_user.address_state, 'State')
        self.assertEqual(self.parent_user.address_zip, '12345')

    def test_child_user_has_no_address(self):
        self.assertIsNone(self.child_user.address_street)
        self.assertIsNone(self.child_user.address_city)
        self.assertIsNone(self.child_user.address_state)
        self.assertIsNone(self.child_user.address_zip)

    def test_child_user_belongs_to_parent(self):
        self.assertEqual(self.child_user.parent, self.parent_user)
