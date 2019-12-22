from django.db import models
import django
# import django.utils.timezone.now

# Create your models here.


class Tasks(models.Model):
    now = django.utils.timezone.now
    name = models.CharField(max_length=35)
    description = models.TextField()
    task_type = models.CharField(max_length=50, default='random')
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
