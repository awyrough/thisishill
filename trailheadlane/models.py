from django.db import models


class Asset(models.Model):
    """
    FX Asset Model
    """
    name = models.TextField()
    base_currency = models.TextField()
    quote_currency = models.TextField()

