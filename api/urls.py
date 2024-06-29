from django.urls import path
from .views import get_student, get_all_student, get_group_student, completed_problem, team_is_problem
urlpatterns = [
    path('user/<username>/', get_student),
    path('users/', get_all_student),
    path('group/<group>/', get_group_student), 
    path('train/<id>/', completed_problem),
    path('train/<group>/<team>/', team_is_problem),
]