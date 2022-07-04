from django.contrib import admin
from baseapp.models import *

# Register your models here.
admin.site.register(user)
admin.site.register(user_follower)
admin.site.register(user_friend)
admin.site.register(user_message)
admin.site.register(user_post)
admin.site.register(group)
admin.site.register(group_member)
admin.site.register(group_message)
admin.site.register(group_follower)