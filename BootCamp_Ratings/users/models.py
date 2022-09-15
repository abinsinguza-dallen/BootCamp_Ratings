
# Create your models here.


from django.db import models
from django.utils import timezone

# Create your models here.
class Students(models.Model):
    student_name= models.CharField(max_length=15,null=True)
    student_id= models.SmallIntegerField(null=True)
    student_course= models.CharField( max_length=20, null=True)
    student_choices=(
        ('Very Unsatisfied','-2'),
        ('Unsatisfied','-1'),
        ('Nuetral','0'),
        ('Satisfied','1'),
        ('Very Satisfied','2')
    )
    student_scores= models.CharField(max_length=30,choices=student_choices,null=True)
    gender_choices=(
        ('F','female'),
        ('M','male'),
        ('O', 'other')
    )
    gender=models.CharField(max_length=10,choices=gender_choices, null=True)
    date=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.student_scores    

    
class LearningFacilitators(models.Model):
    lf_name= models.CharField(max_length=30,null=True)
    students_choices=(
        ('So unsatisfied','-2'),
        ('Unsatisfied','-1'),
        ('Nuetral','0'),
        ('Satisfied','1'),
        ('So satisfied','2')
    )
    students_scores= models.CharField(max_length=30,choices=students_choices,null=True)
    date=models.DateTimeField(default=timezone.now)


  
        
