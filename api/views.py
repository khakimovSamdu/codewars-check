from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import requests
from .models import Student, Problem, Mavzu, Group
# Create your views here.


def get_student(request: HttpRequest, username: str):
    if request.method == 'GET':
        url = f'https://www.codewars.com/api/v1/users/{username}/'
        get_data_all = requests.get(url=url).json()
        student_data = {
            'id':get_data_all['id'],
            'username': get_data_all['username'],
            'name': get_data_all['name'],
            'honor': get_data_all['honor'],
            'clan': get_data_all['clan'],
            'ranks': get_data_all['ranks']['overall']['name'],
            'totalCompleted': get_data_all['codeChallenges']['totalCompleted']
        }
        return JsonResponse(student_data, safe=False)
    else:
        return HttpResponse("Method not GET")

def get_all_student(request: HttpRequest) -> dict:
    if request.method == "GET":
        data = Student.objects.all()
        result = []
        for user in data:
            username = user.usrename
            url = f'https://www.codewars.com/api/v1/users/{username}/'
            get_data_all = requests.get(url=url).json()
            student_data = {
                'id': get_data_all['id'],
                'username': get_data_all['username'],
                'name': get_data_all['name'],
                'honor': get_data_all['honor'],
                'clan': get_data_all['clan'],
                'ranks': get_data_all['ranks']['overall']['name'],
                'totalCompleted': get_data_all['codeChallenges']['totalCompleted']
            }
            # print(student_data)
            result.append(student_data)
        return JsonResponse(result, safe=False)
    else:
        return HttpResponse("Method not GET")    

def get_group_student(request: HttpRequest, group: str):
    if request.method == "GET":
        data = Student.objects.all()
        result = []
        problems = Problem.objects.all()
        ls = []
        for i in problems:
            print(i)
        print(ls)
        for user in data:
            username = user.usrename
            url = f'https://www.codewars.com/api/v1/users/{username}/'
            
            get_data_all = requests.get(url=url).json()
            student_data = {
                'id':get_data_all['id'],
                'username': get_data_all['username'],
                'name': get_data_all['name'],
                'honor': get_data_all['honor'],
                'clan': get_data_all['clan'],
                'ranks': get_data_all['ranks']['overall']['name'],
                'totalCompleted': get_data_all['codeChallenges']['totalCompleted']
            }
            
            if student_data['clan'] == group:
                
                result.append(student_data)
        return JsonResponse(result, safe=False)
    else:
        return HttpResponse("Method not GET")    

def completed_problem(request: HttpRequest, id):
    if request.method == "GET":
        users = Student.objects.all()
        
        result = {}
        for user in users:
            username = user.usrename
            url = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/completed'
            get = requests.get(url=url).json()
            data_problem = get['data']
            print(len(data_problem))
            c = 0
            for problem in data_problem:
                if problem['id']==id:
                    c+=1
            if c!=0:
                result[username] = True
            else:
                result[username] = False
        return JsonResponse(result)
    else:
        return HttpResponse("Method not GET")
