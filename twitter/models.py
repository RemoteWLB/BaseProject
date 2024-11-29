from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class Twitter(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    uuid = ShortUUIDField(length=16, max_length=20, db_index=True)
    t_id = models.CharField(max_length=100, db_index=True)
    tu_id = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    nickname = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    avatar = models.CharField(max_length=1000)
    content = models.CharField(max_length=3000)
    media = models.JSONField(null=True, blank=True)
    hash_tag = models.JSONField(null=True, blank=True)
    local_media = models.JSONField(null=True, blank=True)
    storage_size = models.IntegerField(null=True, blank=True)
    relat_count = models.IntegerField(default=0)
    favorite_count = models.IntegerField(null=True, blank=True)
    quote_count = models.IntegerField(null=True, blank=True)
    reply_count = models.IntegerField(null=True, blank=True)
    retweet_count = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "twiiter"
        db_table = "twiiter"
        
        
class MappTree(models.Model):
    
    NodeType = [
        [1, "dir"],
        [2, "file"]
    ]
    
    id = models.AutoField(primary_key=True, verbose_name="ID")
    uuid = ShortUUIDField(length=16, max_length=20, db_index=True)
    user_id = models.IntegerField()
    parent_id = models.CharField(max_length=100, null=True, blank=True)
    is_root = models.BooleanField(default=False)
    node_type = models.IntegerField(choices=NodeType)
    node_name = models.CharField(max_length=100)
    path_name = models.CharField(max_length=1000)
    instance_key = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "mapp_tree"
        db_table = "mapp_tree"
    