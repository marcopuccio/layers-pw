from django.db import models

class VerificatorAPI(models.Model):
    """
    Initiate a Instance of an verificator to validate the CUIT verificator
    Number
    """
    name = models.CharField(max_length=255)
    date = models.DateTimeField('Creation Day')

    def __unicode__(self):
        return self.name

    def add_one(self, num):
        num += 1
        return num
