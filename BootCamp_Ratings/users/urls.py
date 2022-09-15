from django.urls import path


from . import views


urlpatterns=[
    path("Register/",views.RegStudents, name="registration"),
    path("Students/",views.students,name="liststudents"),
    path("facilitator/",views.learning, name="facilitatorregistration"),
    path("facilitators/",views.facilitators,name="listsfacilitators")
    

]

