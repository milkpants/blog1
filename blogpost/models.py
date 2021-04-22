from django.db import models

class SampleModel(models.Model):
    title = models.CharField(max_length= 100)
    number = models.IntegerField()

CATEGORY = (('buseness', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
# Create your models here.
