from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('''
		<h1>UNIFAFIBE</h1><br>
		<h2>Programação Orientada a Objetos</h2><br>
		<h3>Prof. MSc. Andrey Omar Mozo Uscamayta</h3><br>
		<h2>2021</h2>''')