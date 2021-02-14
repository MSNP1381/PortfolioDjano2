from django.db import models

# Create your models here.
class Blog_model(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/")
    body=models.TextField(blank=True)
    pub_date=models.DateField(auto_now_add=True)
