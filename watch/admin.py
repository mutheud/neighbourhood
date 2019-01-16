from django.contrib import admin
from watch.views import *
from .models import Business,Profile,NeighborHood,Post,Comment
# Register your models here.

admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(NeighborHood)
admin.site.register(Post)
admin.site.register(Comment)
