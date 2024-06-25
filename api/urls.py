from django.urls import path
from .views import get_student, get_all_student, get_group_student
urlpatterns = [
    path('user/<username>/', get_student),
    path('users/', get_all_student),
    path('group/<group>/', get_group_student), 
    

]