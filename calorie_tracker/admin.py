from django.contrib import admin

from .models import *

admin.site.register(Dish)
admin.site.register(Meal)
admin.site.register(Product)
admin.site.register(Day)
admin.site.register(Weight)

