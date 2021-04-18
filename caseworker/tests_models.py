from django.test import TestCase
from datetime import date
import uuid
from caseworker.models import Country, PostalCode, Address, Company


class CaseModelTest(TestCase):

    def setUp(self):
        self.county_name_t = Country.objects.create(name='Denmark')

        self.postal_code_t = PostalCode.objects.create(
            post_code='2500', city_name='Valby', country=self.county_name_t
        )

        self.address_t = Address.objects.create(
            street='nybrovej 14',
            post_code=self.postal_code_t
        )
        self.company_t = Company.objects.create(
            name='Enkelte styresle',
            address=self.address_t
        )

    # Test that Status has a status of type str
    def test_country_has_name(self):
        self.assertIsInstance(self.county_name_t.name, str)

    # Test that CaseInfo has guid of type uuid.UUID
    def test_postal_code_has_city_name(self):
        self.assertIsInstance(self.postal_code_t.post_code, str)

    def test_postal_code_has_postal_code(self):
        self.assertIsInstance(self.postal_code_t.city_name, str)

    def test_postal_code_has_country(self):
        self.assertIsInstance(self.postal_code_t.country.name, str)
'''
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
        self.assertEqual(str(self.case1.title), 'Unit test case title 1')

    # Test that created is set to today on Case
    def test_case_created_date(self):
        self.assertEqual(str(self.case1.created), str(date.today()))

    # Test that default value is NEW
    def test_status_created(self):
        self.assertEqual(self.status1.status, Status.NEW)

    def test_status_created_str(self):
        self.assertEqual(str(self.status1), dict(Status.CASESTATUS)[Status.NEW])
'''
