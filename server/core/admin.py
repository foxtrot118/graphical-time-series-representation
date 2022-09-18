from django.contrib import admin

from .models import Values
admin.site.register(Values)


from .models import Returns
admin.site.register(Returns)