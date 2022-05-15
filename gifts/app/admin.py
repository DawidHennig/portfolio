from django.contrib import admin

# Register your models here.


from app.models import Category, Institution, Donation  

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
