from django.contrib import admin

from .models import registerd_user
from .models import addProduct
from .models import addReturn
from .models import salesAdd


# Register your models here.
admin.site.register(registerd_user)
admin.site.register(addProduct)
admin.site.register(addReturn)
admin.site.register(salesAdd)

