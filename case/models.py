from django.db import models
from django.urls import reverse
import uuid
# from caseworker.models import User, Company


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

    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    # caseworker = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="caseworker", null=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="status_name",
                               default="Sagen er nyoprettet")

    def __str__(self):  # return the name we will object calls
        return str(self.guid)


class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    case_info = models.ForeignKey(CaseInfo, on_delete=models.CASCADE, related_name="case_case_info")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case:case-detail', kwargs={'pk': self.pk})


'''
# uuid = uuid.uuid4()
# print (uuid_nr.default())

status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    # updated = models.DateTimeField(auto_now=True)
    # case_post = models.DateTimeField(default=timezone.now) # finde tid som en post bliver gemt
    # image = models.ImageField(upload_to="images")
    # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    STATUS_CHOICES = (
        ('n', 'None'),
        ('u', 'Under_behandling'),
        ('a', 'Afgjort'),
        ('i', 'ignored'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    e = Case.objects.get(id=3)
    print("caseinfoooooo:", e.case_info_id)
    c = CaseInfo.objects.get(pk=1)
    c = Case.objects.get(id=1)
Mediaforocase = Media.objects.filter(case=c)

class Media(models.Model):
    filename = models.CharField(max_length=200)
    time_of_delete = models.DateField(auto_now=True, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    # images = models.FileField(upload_to="images", blank=True)
    case_info = models.ForeignKey(CaseInfo, on_delete=models.CASCADE, related_name="media_case_info")

    class Meta:
        verbose_name = "media"
        verbose_name_plural = "media"

    def __str__(self):  # return the name we will object calls
        return self.filename
'''
