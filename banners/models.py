from django.db import models


class MainBanner(models.Model):
    img = models.FileField()
    link = models.CharField(max_length=255, blank=True, null=True)

class Banner(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    img = models.FileField()
    order = models.IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return self.title
 
# Create your models here.
