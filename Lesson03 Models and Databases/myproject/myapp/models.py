from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    status = models.CharField(max_length=10 ,default= 'ready')

    def __str__(self):
        return f"{self.author}, {self.title}, {self.published_date}"