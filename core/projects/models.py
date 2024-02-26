from django.db import models
from user.models import MyUser
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to="self", on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # project = models.ForeignKey() ForeignKey to Project table
    rate_score = models.PositiveSmallIntegerField()
    comment = models.TextField()

class ProjectStatus(models.TextChoices):
    in_process = 'In Process', 'in_process'
    waiting = 'Waiting', 'waiting'
    archive = 'Archive', 'archive'
    done = 'Done', 'done'

class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    status = models.CharField(max_length=64, choices=ProjectStatus.choices, default=ProjectStatus.waiting)
    category = models.ForeignKey(Category,  related_name='catrgory_project', on_delete=models.CASCADE)
    employer = models.ForeignKey(MyUser, related_name='employer_project', on_delete=models.CASCADE)
    expected_price = models.PositiveBigIntegerField()
    expected_time = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    done_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]
    

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
    