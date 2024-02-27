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
    title = models.CharField(max_length=512)
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
        return self.title
    

