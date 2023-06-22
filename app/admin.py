from django.contrib import admin
from .models import *
# from django.forms import widgets
from .forms import CustomTimeField
class blogadmin(admin.ModelAdmin):
    list_display=['title','price','type','name']
    search_fields=['title','type','name']
    list_filter=['title','type','price','name']
    formfield_overrides = {
        models.TimeField: {'form_class': CustomTimeField},
    }
    # formfield_overrides = {models.TimeField: {'widget': widgets.TimeInput(format='%I:%M %p')}}
    fieldsets=[
        (
            'Info',
            {
                'fields':['title','price','type','schedule_from','schedule_to']
            }
        ),
        (

            
            'Advanced options',
            {
                "classes": ["collapse"],
                "fields":['name','desc','images','Total_Seat','long_desc']
            }
        )

    ]


# Register your models here.
admin.site.register(blog,blogadmin)
admin.site.register(trainer)
admin.site.register(domain)
admin.site.register(pricing)
admin.site.register(features)