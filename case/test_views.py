from django.test import TestCase, Client
from case.models import Case, CaseInfo, Status
from caseworker.models import Company, Country, PostalCode, Address
from django.urls import reverse
from django.views.generic import TemplateView
from case.views import CaseListView


class TestCaseView(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['case1'])
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
        self.case_info1 = CaseInfo.object.create(
            status=self.status1,
            company=self.company1
        )
        self.case1 = Case.objects.create(
            title='Unit test case title 1',
            description='Unit test case description 1',
            case_info=self.case_info1)
        self.case1.save()

    class HomeView(TemplateView):
        template_name = 'case/case.html'

        def get_context_data(self, **kwargs):
            kwargs['environment'] = 'Production'
            return super().get_context_data(**kwargs)

            print("helllloooo", self.case1)

        def test_case_listview(self):
            response = self.client.get(reverse('list'))

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'case/case.html')
