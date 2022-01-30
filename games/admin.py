from django.contrib import admin

from games.models import gamesrev,myrev,contact

# Register your models here.
admin.site.register(gamesrev)
admin.site.register(myrev)
admin.site.register(contact)