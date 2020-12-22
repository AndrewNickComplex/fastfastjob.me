from django.test import TestCase
from .models import Job, User, Category, Application, Jobber
# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):

        u1 = User.objects.create(
            username='andrew',
            last_name='Siah',
            first_name='Andrew',
            contact_method='whatsapp',
            gender='male',
            )

        u2 = User.objects.create(
            username='nick',
            first_name='Nicholas',
            last_name='Yeo',
            gender = 'others',
            contact_method = 'email',
            email = "nick@nick.com"
            )
        
        t1 = Tag.objects.create(
            title = "gardening")

        t2 = Tag.objects.create(
            title = 'delivery')

        j1 = Job.objects.create(
            created_by = u1,
            title = 'Deweed my lawn',
            description = 'Come my house to deweed my 40ft lawn',
            tag = t1,
            estimate_pay = 25,
            number_of_positions = 2
            )

        j2 = Job.objects.create(
            created_by = u2,
            title = 'Bring me clothes',
            description = 'Buy me white shirt from uniqlo and deliver to me',
            tag = t2,
            estimate_pay = 5,
            number_of_positions = 1
            )

        j3 = Job.objects.create(
            created_by = u2,
            title = 'Bring me pants',
            description = 'Pants from uniqlo and deliver to me',
            tag = t2,
            estimate_pay = 5,
            number_of_positions = 1
            )

    def test_job_created_count(self):
        u = User.objects.get(last_name='Yeo')
        self.assertEqual(u.jobs_created.count(), 2)
