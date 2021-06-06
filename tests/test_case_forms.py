from django.test import TestCase, Client
from case.forms import AnonymousForm
import uuid


class TestForms(TestCase):
    def setUp(self):
        self.client = Client()

        self.guid = uuid.uuid4()

    def test_ReportLoginViewGuid(self):
        form = AnonymousForm(data={
            'guid': self.guid
        })
        self.assertTrue(form.is_valid())

    def test_ReportLoginViewString(self):
        form = AnonymousForm(data={
            'guid': 'bare_string122'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_ReportLoginViewGuidString(self):
        form = AnonymousForm(data={
            'guid': '4916d99e-8ccf-49bd-ad77-4e1c7aa90f8c'
        })
        self.assertTrue(form.is_valid())

    def test_ReportLoginViewLikeGuidString(self):
        form = AnonymousForm(data={
            'guid': '4916d99e-8ccf-49bd-ad77-4e1c7f8c'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_ReportLoginViewLikeAzGuidString(self):
        form = AnonymousForm(data={
            'guid': 'c98baaf9-e8c3-4332-823d-79c726d9vd02'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
