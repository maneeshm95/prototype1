from django.contrib import admin
from .models import Patient

#admin.site.register(Patient)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','age','gender','dateofbirth']
    prepopulated_fields = {
        'slug' : ['first_name','last_name']
    }


admin.site.register(Patient,PatientAdmin)