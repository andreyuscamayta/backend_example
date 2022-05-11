from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseNotFound
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
	return HttpResponse('''
		<h1>UNIFAFIBE</h1><br>
		<h2>Programação Orientada a Objetos</h2><br>
		<h3>Prof. MSc. Andrey Omar Mozo Uscamayta</h3><br>
		<h2>2022</h2>''')

def users(request):
	objects = User.objects.all()
	user_list = []
	for usr in objects:
		user_list.append(convert_user_object_to_dic(usr))
	return JsonResponse(user_list, safe=False)

def get_user(request, user_id):
	user = User.objects.get(pk=user_id)
	return JsonResponse(convert_user_object_to_dic(user), safe=False)

def validate_user(request):
	print(request.body)
	body = json.loads(request.body)
	user = User.objects.get(username=body["username"])
	if(user.check_password(body["password"])):
		return JsonResponse(convert_user_object_to_dic(user), safe=False)
	return HttpResponseNotFound('<h1>User not found</h1>')

@csrf_exempt
def save_user(request):
	if request.method == "POST":
		body = json.loads(request.body)
		user = User.objects.create_user(
			body["username"],
			body["email"],
			body["password"],
			)
		user.first_name = body["first_name"]
		user.last_name = body["last_name"]
		user.save()
		return JsonResponse(convert_user_object_to_dic(user), safe=False)

def convert_user_object_to_dic(user):
	return {
			"id":user.id,
			"username":user.username,
			"first_name":user.first_name,
			"last_name":user.last_name,
			"email":user.email
			}
