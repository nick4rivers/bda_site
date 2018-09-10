from django.db import models

# Create your models here.


class ContactRequest(models.Model):
    CreatedDateTime = models.DateTimeField(auto_now=True)
    ModifiedDateTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.name, self.resolved)
