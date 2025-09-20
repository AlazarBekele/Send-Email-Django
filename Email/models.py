from django.db import models

# Create your models here.

class IndexBackground (models.Model):

    NamePic = models.CharField(max_length=20)
    MainPicture = models.ImageField()

    def __str__(self):
        return self.NamePic