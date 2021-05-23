from django.test import TestCase, Client
from case.models import Case, CaseInfo, Status
from caseworker.models import Company, Country, PostalCode, Address
from django.urls import reverse


class TestCaseView(TestCase):

    def setUp(self):
        self.client = Client()

        self.country_name1 = Country.objects.create(
            name='Denmark'
        )

        self.postal_code1 = PostalCode.objects.create(
            post_code='2500', city_name='Valby', country=self.country_name1
        )

        self.address1 = Address.objects.create(
            street='nybrovej 14',
            post_code=self.postal_code1
        )

        self.company1 = Company.objects.create(
            name='microsof',
            address=self.address1
        )

        self.status1 = Status.objects.create()
        self.case_info1 = CaseInfo.objects.create(
            status=self.status1,
            company=self.company1
        )
        self.case1 = Case.objects.create(
            title='Unit test case title 1',
            description='Unit test case description 1',
            case_info=self.case_info1
        )
        self.case1.save()

    def test_CaseListView_Get(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case/case.html')

    def test_CaseCreateView_Post(self):
        self.detail_url = reverse('case:case-create')
        response = self.client.post(self.detail_url, {
            'title': 'Unit test case title 1',
            'description': 'Unit test case description 1',
            'case_info': self.case_info1
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case/case_form.html')

    def test_CaseDetailView_Post(self):
        self.detail_url = reverse('case:case-view')
        print("helllloooooo", self.detail_url)
        case_id = Case.objects.latest('pk')
        response = self.client.get(self.detail_url, kwargs={'pk': case_id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.case1.case_info.company.name, 'microsof')
    '''
    def test_CaseDetailView_Post(self):
        self.detail_url = reverse('case:case-detail', args='1')
        print("hhhhhhhhhhh", self.detail_url)
        self.case_id = Case.objects.latest('pk')
        response = self.client.get(self.detail_url, kwargs={'pk': self.case_id})
        print("Hellllll", response.client)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.case1.case_info.company.name, 'microsof')

    def test_CaseDeleteView_Post(self):

        case_id = Case.objects.latest('pk')
        self.detail_url = reverse('case:case-delete', args='1')
        print("Hellllll",self.detail_url)
        response = self.client.get(self.detail_url, kwargs={'pk': case_id})
        print("Hellllll", response)
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(self.case1.case_info.company.name, 'microsof')

'''
