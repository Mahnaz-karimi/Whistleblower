from django.test import TestCase, Client
from datetime import date
import uuid
from case.models import Case, Status, CaseInfo
from caseworker.models import Country, PostalCode, Address, Company


class CaseModelTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.country_name1 = Country.objects.create(name='Denmark')
        self.postal_code1 = PostalCode.objects.create(post_code='2500', city_name='bynavn', country=self.country_name1)
        self.address1 = Address.objects.create(street='adress 14', post_code=self.postal_code1)
        self.company1 = Company.objects.create(name='Company1', address=self.address1)
        self.status1 = Status.objects.create()
        self.case_info1 = CaseInfo.objects.create(status=self.status1, company=self.company1)
        self.case1 = Case.objects.create(title='Title 1', description='Description 1', case_info=self.case_info1)
        self.case_info1.save()
        self.case1.save()

    # Test that Status has a status of type str
    def test_status_has_status(self):
        self.assertIsInstance(self.status1.status, str)

    # Test that CaseInfo has guid of type uuid.UUID
    def test_case_info_has_guid(self):
        self.assertIsInstance(self.case_info1.guid, uuid.UUID)

    # Test that Case has title of type str
    def test_case_has_title(self):
        self.assertIsInstance(self.case1.title, str)

    # Test that Case has description of type str
    def test_case_has_description(self):
        self.assertIsInstance(self.case1.description, str)

    # Test that Case has created timestamp of type date
    def test_case_has_created(self):
        self.assertIsInstance(self.case1.created, date)

    # Test that __str__ is implemented on Case
    def test_case_title(self):

        self.assertEqual(self.case1.title, 'Title 1')

    # Test that created is set to today on Case
    def test_case_created_date(self):
        self.assertEqual(str(self.case1.created), str(date.today()))

    # Test that case-info is the same
    def test_case_case_info(self):
        self.assertEqual(self.case1.case_info, self.case_info1)

    # Test that default value is NEW
    def test_status_created(self):
        self.assertEqual(self.status1.status, Status.NEW)

    def test_status_created_str(self):
        self.assertEqual(str(self.status1), dict(Status.CASESTATUS)[Status.NEW])

    def test_case_instance(self):
        self.assertTrue(isinstance(self.case1, Case))

    def test_case1_title(self):
        self.assertEqual(str(self.case1), "Title 1")
