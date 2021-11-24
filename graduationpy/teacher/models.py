from django.db import models

# Create your models here.


class Quote(models.Model):
    quote = models.CharField(max_length=200)

    class Meta:
        db_table = 'quote'

    pass
