from django.test import TestCase
import uuid
from caseworker.models import Country, PostalCode, Address, Company


class CaseModelTest(TestCase):

    def setUp(self):
        self.country_name_t = Country.objects.create(name='Denmark')

        self.postal_code_t = PostalCode.objects.create(
            post_code='2500', city_name='Valby', country=self.country_name_t
        )

        self.address_t = Address.objects.create(
            street='nybrovej 14',
            post_code=self.postal_code_t
        )
        self.company_t = Company.objects.create(
            name='Enkelte styresle',
            address=self.address_t
        )

    def test_country_has_name(self):
        self.assertIsInstance(self.country_name_t.name, str)

    def test_country_name(self):
        self.assertEqual(self.country_name_t.name, 'Denmark')

    def test_postal_code_has_city_name(self):
        self.assertIsInstance(self.postal_code_t.post_code, str)

    def test_postal_code_city_name(self):
        self.assertEqual(self.postal_code_t.city_name, 'Valby')

    def test_postal_code_has_postal_code(self):
        self.assertIsInstance(self.postal_code_t.city_name, str)

    def test_postal_code_postal_code(self):
        self.assertEqual(self.postal_code_t.post_code, '2500')

    def test_postal_code_has_country(self):
        self.assertIsInstance(self.postal_code_t.country.name, str)

    def test_postal_code_country(self):
        self.assertEqual(self.postal_code_t.country.name, 'Denmark')

    def test_address_has_street(self):
        self.assertIsInstance(self.address_t.street, str)

    def test_address_street(self):
        self.assertEqual(self.address_t.street, 'nybrovej 14')

    def test_address_has_postcode(self):
        self.assertIsInstance(self.address_t.post_code.city_name, str)

    def test_address_postcode(self):
        self.assertEqual(self.address_t.post_code.city_name, 'Valby')

    def test_company_has_name(self):
        self.assertIsInstance(self.company_t.name, str)

    def test_company_name(self):
        self.assertEqual(self.company_t.name, 'Enkelte styresle')

    def test_company_has_guid(self):
        self.assertIsInstance(self.company_t.guid, uuid.UUID)

    def test_company_has_address_street(self):
        self.assertEqual(self.company_t.address.street, 'nybrovej 14')

    def test_company_address_street(self):
        self.assertIsInstance(self.company_t.address.street, str)

    def test_company_has_address_postcode(self):
        self.assertEqual(self.company_t.address.post_code.post_code, '2500')

    def test_company_address_postcode(self):
        self.assertIsInstance(self.company_t.address.post_code.post_code, str)
