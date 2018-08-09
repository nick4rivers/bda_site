from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedDateTime = models.DateTimeField(auto_now=True)
    ModifiedDateTime = models.DateTimeField(auto_now_add=True)
    ProjectName = models.CharField(max_length=50)
    ProjectDescription = models.TextField()
    ProjectImage = models.ImageField(upload_to='project_images/')
    InstallDate = models.DateField()
    TreatmentLength = models.FloatField()
    TotalStructures = models.IntegerField()
    ProjectAffiliation = models.CharField(max_length=60)
    AffiliationImage = models.ImageField(upload_to='affiliation_images/')
    PrimaryContactName = models.CharField(max_length=60)
    PrimaryContactEmail = models.EmailField(max_length=100)

    def __str__(self):
        return self.ProjectName
