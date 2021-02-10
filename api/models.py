from django.db import models

class Api(models.Model):
    title = models.CharField(max_length = 300)
    url = models.URLField(max_length = 1000)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.title) 