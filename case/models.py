from django.db import models
from django.urls import reverse
import uuid
from caseworker.models import Company
from django.contrib.auth.models import User


class Status(models.Model):
    NEW = 'Ny'
    PROCESSING = 'Behandles'
    CLOSED = 'Lukket'
    REJECTED = 'Afvist'

    CASESTATUS = [
        (NEW, 'Sagen er nyoprettet'),
        (PROCESSING, 'Sagen behandles'),
        (CLOSED, 'Sagen er lukket'),
        (REJECTED, 'Sagen er afvist'),
    ]

    status = models.CharField(
        max_length=32,
        choices=CASESTATUS,
        default=NEW
    )

    def __str__(self):
        return dict(self.CASESTATUS)[self.status]


class CaseInfo(models.Model):
    guid = models.UUIDField(
         default=uuid.uuid4,
         editable=False,
         unique=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    caseworker = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="caseworker", null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="status_name",
                               default="Sagen er nyoprettet")

    def __str__(self):  # return the name we will object calls
        return str(str(self.company) + "  Case number:  " + str(self.guid))


class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    case_info = models.ForeignKey(CaseInfo, on_delete=models.CASCADE, related_name="case_case_info")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case:case-detail', kwargs={'pk': self.pk})
