from django.test import TestCase
from .models import Membership


class MembershipTest(TestCase):
    # --------------------------------- Test name of membership_type

    def test_str(self):
        test_name = Membership(membership_type="Full Membership")
        self.assertEqual(str(test_name), "Full Membership")
