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
        users = Student.objects.filter(guruh__name__contains=group)
        result = []
        
        for user in users:
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

def team_is_problem(request: HttpRequest, group: str, team: str):
    if request.method == "GET":
        users = Student.objects.filter(guruh__name__contains=group)
        result = []
        problems = Problem.objects.filter(mavzu__name__contains=team)
        
        for user in users:
            username = user.usrename
            
            url_totalPages = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/completed'
            totalPages = int(requests.get(url=url_totalPages).json()['totalPages'])
            done = 0
            failed = 0
            masala_id_data = []
            for total in range(totalPages):       
                url_completed = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/completed/?page={total}'
                get_completed = requests.get(url=url_completed).json()['data']
                for masala in get_completed:
                    masala_id_data.append(masala['id'])

            for problem in problems:
                masala_id = problem.id
                if masala_id in masala_id_data:
                    done += 1
                else:
                    failed += 1

            student_data = {
                'username': username,
                'done': done,
                'failed': failed
            }
            result.append(student_data)

        return JsonResponse(result, safe=False)
    else:
        return HttpResponse("Method not GET")    