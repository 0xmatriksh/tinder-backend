from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to = 'profile',null=True)

    def __str__(self):
        return self.name
    @property
    def ext_link(self):
        return f'http://127.0.0.1:8000{self.image.url}'