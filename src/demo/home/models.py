from django.db import models

# Create your models here.

class UserQuery(models.Model):
    query = models.CharField(max_length=200)
    query_date = models.DateTimeField("date queried", auto_now_add=True)

    def __str__(self):
        return self.query