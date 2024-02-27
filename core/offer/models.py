from django.db import models

from user.models import MyUser
from projects.models import Project

import uuid
# Create your models here.

class Offer(models.Model):

    class OfferStatus(models.TextChoices):
        accepted = 'Accepted', 'accepted'
        rejected = 'Rejected', 'rejected'
        pending = 'Pending', 'pending'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey(Project, related_name='project_offer', on_delete=models.CASCADE)
    service_man = models.ForeignKey(MyUser, related_name='service_project', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=64, choices=OfferStatus.choices, default=OfferStatus.pending)
    finish_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_id.content[:30] + ' --- ' + self.status