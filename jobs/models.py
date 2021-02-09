from django.db import models


# Create your models here.
class Job(models.Model):
    imgae = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.summary
