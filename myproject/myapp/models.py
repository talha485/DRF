from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return self.title
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.first_name + " " + self.last_name
