import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mail = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.mail})"

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} ({len(self.members.all())} member)"