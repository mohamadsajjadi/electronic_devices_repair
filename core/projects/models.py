from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to="self", on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()


class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # project = models.ForeignKey() ForeignKey to Project table
    rate_score = models.PositiveSmallIntegerField()
    comment = models.TextField()
