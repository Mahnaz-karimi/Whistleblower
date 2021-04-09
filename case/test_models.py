from django.test import TestCase
from datetime import date
import uuid
from case.models import Case, Media, Status, CaseInfo


class CaseModelTest(TestCase):

    def setUp(self):
        self.status1 = Status.objects.create()

        self.case_info1 = CaseInfo.objects.create(
            status=self.status1
        )

        self.case1 = Case.objects.create(
            title='Unit test case title 1',
            description='Unit test case description 1',
            case_info=self.case_info1
        )

        self.media1 = Media.objects.create(
            filename='Unit test media filename 1',
            time_of_delete=None,
            case=self.case1
        )

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

    # Test that Media has a filename of type str
    def test_media_has_filename(self):
        self.assertIsInstance(self.media1.filename, str)

    # Test that Media has a time_of_delete of type date
    def test_media_has_time_of_delete(self):
        self.media1.time_of_delete = date.today()
        self.assertIsInstance(self.media1.time_of_delete, date)

    # Test that Media has a created of type date
    def test_media_has_created(self):
        self.assertIsInstance(self.media1.created, date)

    # Test that __str__ is implemented on Case
    def test_case_title(self):
        self.assertEqual(str(self.case1.title), 'Unit test case title 1')

    # Test that created is set to today on Case
    def test_case_created_date(self):
        self.assertEqual(str(self.case1.created), str(date.today()))

    # Test that __str__ is implemented on Media
    def test_media_title(self):
        self.assertEqual(str(self.media1.filename), 'Unit test media filename 1')

    # Test that created is set to today on Media
    def test_media_created(self):
        self.assertEqual(str(self.media1.created), str(date.today()))

    # Test that default value is NEW
    def test_status_created(self):
        self.assertEqual(self.status1.status, Status.NEW)

    def test_status_created_str(self):
        self.assertEqual(str(self.status1), dict(Status.CASESTATUS)[Status.NEW])
