from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html')

def eggs(request):
	return HttpResponse("<h1>Eggs are White </h1>")

def password(request):
#Either list can be created similar to lower_char or upper_char way.both options are 
#mentioned for clarity and learning purpose
	the_password = ' '
	total_char =[]
	lower_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
	'r','s','t','u','v','w','x','y','z']
	upper_char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	special_char = list('~!@#$%^&*()')
	
	total_char.extend(lower_char)

	if request.GET.get('uppercase'):
		total_char.extend(upper_char)

	if request.GET.get('numbers'):
		total_char.extend(numbers)

	if request.GET.get('special'):
		total_char.extend(special_char)
	
	length = int(request.GET.get('length',8))

	for i in range(length):
		the_password = the_password + random.choice(total_char)

	return render(request,'generator/password.html',{"password":the_password})

def about(request):
	return render(request,'generator/about.html')
	