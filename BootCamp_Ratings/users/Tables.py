from dataclasses import fields
from pyexpat import model
from django import Tables
from . import models


class StudentsRegistrationTables(Tables.ModelForm):
    class Meta:
        model=models.Students
        fields="__all__"
        
        
class FacilitatorsTables(Tables.ModelForm):
    class Meta:
        model=models.LearningFacilitators
        fields="__all__"        