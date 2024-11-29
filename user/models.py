from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = ShortUUIDField(length=16, max_length=20, db_index=True)

    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    avatar = models.CharField(max_length=500, blank=True, null=True)
    
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.BooleanField(default=False)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return '{0} | {1}'.format(self.nickname, self.email)