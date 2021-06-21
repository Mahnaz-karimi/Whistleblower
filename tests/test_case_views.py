from django.test import TestCase, Client
from case.models import Case, CaseInfo, Status
from caseworker.models import Company, Country, PostalCode, Address
from django.urls import reverse
import uuid
from case.forms import AnonymousForm


class TestCaseView(TestCase):

    def setUp(self):
        self.client = Client()
        self.guid = uuid.uuid4()
        self.country_name1 = Country.objects.create(name='Denmark')
        self.postal_code1 = PostalCode.objects.create(
            post_code='2100', city_name='copenhagen', country=self.country_name1
        )

        self.address1 = Address.objects.create(street='street1', post_code=self.postal_code1)
        self.company1 = Company.objects.create(name='company1', address=self.address1)
        self.status1 = Status.objects.create()
        self.case_info1 = CaseInfo.objects.create(status=self.status1, company=self.company1)
        self.case_info1.save()
        self.case1 = Case.objects.create(title='Title 1', description='Description 1', case_info=self.case_info1)
        self.case1.save()

    def test_CaseInfo_Cases_ListView(self):
        case = Case.objects.latest('pk')
        self.detail_url = reverse('case:case-create-new', args=[case.case_info.id])
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 302)  # redirect til login side

    def test_CaseInfo_DeleteView(self):
        case_info = CaseInfo.objects.latest('pk')
        self.detail_url = reverse('case:caseinfo-delete', args=[case_info.id])
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 302)

    def test_CaseInfoUpdateView(self):
        case = Case.objects.latest('pk')
        self.detail_url = reverse('case:caseinfo-update', args=[case.case_info.id])
        response = self.client.post(self.detail_url, {
            'status': self.status1,
            'company': self.company1,
        })
        self.assertEqual(response.status_code, 200)

    def test_Case_new_CreateView_Post(self):
        case = Case.objects.latest('pk')
        self.detail_url = reverse('case:caseinfo-cases-view', args=[case.case_info.id])
        response = self.client.post(self.detail_url, {
            'title': 'Unit test case title 1',
            'description': 'Unit test case description 1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=" + self.detail_url)  # fordi vi ikke har logget ind


    def test_Case_DetailView_Post(self):
        case = Case.objects.latest('pk')
        self.detail_url = reverse('case:case-detail', args=[case.id])
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=" + self.detail_url)
        self.assertEqual(self.case1.case_info.company.name, 'company1')

    def test_Case_DeleteView(self):
        case = Case.objects.latest('pk')
        self.delete_url = reverse('case:case-delete', args=[case.id])
        response = self.client.get(self.delete_url)
        self.assertEqual(response.url, "/accounts/login/?next=" + self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_Report_LoginView(self):
        self.detail_url = reverse('case:report-login')
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case/report_login.html')

    def test_ReportCreateView(self):
        self.detail_url = reverse('case:new-report', args=[self.case_info1.id])
        response = self.client.get(self.detail_url)
        self.assertEqual(response.url, "/case/login/")  # Den bliver redirect til login side fordi mangler session
        self.assertEqual(response.status_code, 302)

    def test_RevisitLoginViewWithValidData(self):
        data = {"case_info": self.case_info1}
        form = AnonymousForm(data=data)
        response = self.client.get(reverse('case:revisit-login'), args=[self.case_info1.id, form])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case/revisit_login.html')

    def test_RevisitCaseNewCreateView(self):
        case_info = self.case_info1
        response = self.client.get(reverse('case:revisit-case-new', args=[case_info.id]))
        self.assertEqual(response.status_code, 302)  # redirect til login
