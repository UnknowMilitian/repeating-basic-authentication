from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    title = models.CharField(_("Item title"), max_length=250)
    description = models.TextField(_("Item Description"))

    def __str__(self):
        return f"Item - {self.title}"
