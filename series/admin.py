from django.contrib import admin

from series.models import seriesrev,myrev,contact

# Register your models here.
admin.site.register(seriesrev)
admin.site.register(myrev)
admin.site.register(contact)