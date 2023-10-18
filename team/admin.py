from django.contrib import admin

from .models import Team, Invitation, Plan



# Register your models here.

admin.site.register(Team)
admin.site.register(Invitation)
admin.site.register(Plan)
