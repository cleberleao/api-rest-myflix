from django.http import JsonResponse
from django.shortcuts import render

def users(request):
    if request.method == 'GET':
        user={
            'id':1,
            'nome': 'José'
        }
    return JsonResponse(user, json_dumps_params={'ensure_ascii':False})
