from django.test import TestCase, Client
from case.forms import AnonymousForm
import uuid


class TestForms(TestCase):
    def setUp(self):
        self.client = Client()
        self.guid = uuid.uuid4()

    def test_ReportLoginViewGuid(self):  # En guid
        form = AnonymousForm(data={
            'guid': self.guid
        })
        assert form.is_valid()

    def test_ReportLoginViewGoodGuidString(self):  # En korrakte guid checkes
        form = AnonymousForm(data={
            'guid': '4916d99e-8ccf-49bd-ad77-4e1c7aa90f8c'
        })
        assert form.is_valid()

    def test_ReportLoginViewBadGuidString(self):  # En bad guid checkes
        form = AnonymousForm(data={
            'guid': 'BAD_GUID'
        })
        assert not form.is_valid()
        assert len(form.errors) == 1
