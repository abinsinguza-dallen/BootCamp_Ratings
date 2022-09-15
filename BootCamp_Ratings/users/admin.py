from django.contrib import admin
from .models import Students
from .models import LearningFacilitators
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display=('student_name','student_id','student_scores')
    search_fields=('Student_Name','student_scores')
admin.site.register(Students,StudentsAdmin) 

class LearningAdmin(admin.ModelAdmin):
    list_display=('Name','students_scores')
    search_fields=('Name','students_scores')
admin.site.register(LearningFacilitators,LearningAdmin)    
