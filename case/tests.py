from django.test import TestCase
from case.models import Case, CaseInfo, Status
import uuid


class TestCaseModel(TestCase):

    def setUp(self):

        s = Status.objects.create(status="None")
        u = uuid.uuid4()
        ci = CaseInfo.objects.create(guid=u, status=s)
        self.case = Case.objects.create(title='django', description='det er en test', case_info=ci)

    def test_case_model(self):
        d = self.case
        self.assertTrue(isinstance(d, Case))
        self.assertEqual(str(d), 'django')
