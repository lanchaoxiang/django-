from django.contrib import admin

# Register your models here.
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sex', 'creat_time', 'status', 'profession')
    list_filter = ('sex','status','creat_time')
    fieldsets = ((None,{
        'fields':('name',
                  ('sex','profession'),
                  ('email','phone'),
                  'status',)
    }),)

admin.site.register(Students,StudentsAdmin)