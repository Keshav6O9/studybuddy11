from ast import Index
from pyexpat import model
from tokenize import group
from django.db import models
import email
from django.db import models
import datetime
import os
def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename ="%s%s", (timeNow,old_filename)
    return os.path.join('uploads/',filename)
# Create your models here.

EXAMS = (
    ('upsc','UPSC'),
    ('neet-ug','NEET-UG'),
    ('aiims-ug','AIIMS-UG'),
    ('ugc-net','UGC-NET'),
    ('gate','GATE'),
    ('iit-jee','IIT-JEE'),
    ('ca','CA'),
    ('cat','CAT'),
    ('nda','NDA'),
    ('clat','CLAT'),

)

#-----------------------------------------------------------------User Deatils--------------------------------------------------------
class user(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    mobile = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    passwordHash = models.CharField(max_length=50)
    registerdAt = models.DateTimeField(auto_now=True)
    lastLogin = models.TimeField(auto_now_add=True)
    intro = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)
    exams = models.CharField(choices=EXAMS,max_length=50)


#-----------------------------------------------------------------User Follower--------------------------------------------------------
class user_follower(models.Model):
       id = models.BigAutoField(primary_key=True)
       sourceId = models.ForeignKey(user,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
       targetId = models.ForeignKey(user,on_delete=models.DO_NOTHING)
       type = models.SmallIntegerField()
       createdAt = models.DateTimeField(auto_now=True)
       updatedAt = models.DateTimeField(auto_now_add=True)
    
    #-----------------------------------------------------------------User Friends--------------------------------------------------------
class user_friend(models.Model):
    id = models.BigAutoField(primary_key=True)
    sourceId = models.ForeignKey(user,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    targetId = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

#-----------------------------------------------------------------User message--------------------------------------------------------
class user_message(models.Model):
    id = models.BigAutoField(primary_key=True)
    sourceId = models.ForeignKey(user,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    targetId = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    #-----------------------------------------------------------------User Post--------------------------------------------------------
class user_post(models.Model):
    id = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(user,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    senderId = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)



    # --------------------------------------------------Group Tables--------------------------------------------------------


class group(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdBy = models.ForeignKey(user,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    updatedBy = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=75)
    summary = models.CharField(max_length=200)
    status = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    profile = models.CharField(max_length=200)

class group_member(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupId = models.ForeignKey(group,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    userId = models.ForeignKey(group,on_delete=models.DO_NOTHING)
    status = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class group_message(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupId = models.ForeignKey(group,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    userId = models.ForeignKey(group,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
          
class group_follower(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupId = models.ForeignKey(group,on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    userId = models.ForeignKey(group,on_delete=models.DO_NOTHING)
    type = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)