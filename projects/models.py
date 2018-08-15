from django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.


class Project(models.Model):
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedDateTime = models.DateTimeField(auto_now=True)
    ModifiedDateTime = models.DateTimeField(auto_now_add=True)
    ProjectName = models.CharField(null=True, blank=True, max_length=50)
    StreamName = models.CharField(null=True, blank=True, max_length=50)
    BasinName = models.CharField(null=True, blank=True, max_length=50)
    ProjectDescription = models.TextField(null=True, blank=True)
    ProjectImage = models.ImageField(null=True, blank=True, upload_to='project_images/')
    InstallDate = models.DateField(null=True, blank=True)
    TreatmentLength = models.FloatField(null=True, blank=True)
    TotalStructures = models.IntegerField(null=True, blank=True)
    ProjectAffiliation = models.CharField(null=True, blank=True, max_length=60)
    AffiliationImage = models.ImageField(null=True, blank=True, upload_to='affiliation_images/')
    PrimaryContactName = models.CharField(null=True, blank=True, max_length=60)
    PrimaryContactEmail = models.EmailField(null=True, blank=True, max_length=100)
    ProjectLatitude = models.FloatField(null=True, blank=True)
    ProjectLongitude = models.FloatField(null=True, blank=True)
    geom = models.PointField(null=True, blank=True, srid=4326)

    # Note django keeps PointFields as x: Longitude (-120), y: Latitude (44)
    def get_lat(self):
        return self.geom

    def __str__(self):
        return '{}, ID: {}'.format(self.ProjectName, self.id)

    def __unicode__(self):
        return self.name
