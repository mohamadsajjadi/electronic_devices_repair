from django.db import models

from user.models import MyUser
import uuid
# Create your models here.

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.person} --- {self.amount}'