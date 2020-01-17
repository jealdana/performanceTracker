from django.db import models

# Create your models here.

class Metric(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField("metrics name", max_length=120)
  description = models.TextField()
  value = models.IntegerField()
  date_registered = models.DateField()

  def __str__(self):
    return self.name

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Metric'
    verbose_name_plural = 'Metrics'