from django.db import models

# Create your models here.
class Blog_model(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/",blank=True)
    pub_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+' : '+ self.title

    """
    def summary_body(self):
        return self.body[:70]
    
  
    def Pretty_pub_date(self):
        #search strftime in google
        return self.pub_date.strftime('%a %-d %b %Y')
    """