from django.contrib import admin
from .models import Student, Group, Mavzu, Problem, DayComplated
# Register your models here.

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Mavzu)
admin.site.register(Problem)
admin.site.register(DayComplated)
