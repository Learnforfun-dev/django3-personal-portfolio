from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=100) ## to make the field optional we can add another parater as  blank= 'True
    description= models.CharField(max_length=250)
    image= models.ImageField(upload_to='portfolio/images/') ## for database to use imagefield you have to use Pillow
    url= models.URLField(blank=True)
