from django.db import models

# Create your models here.


class todo(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task