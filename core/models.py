from django.db import models
import datetime
from django.utils.translation import gettext as _

class Anotation(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.name