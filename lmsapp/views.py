from django.shortcuts import render, redirect
from .forms import AndyForm
from .models import AndyModel
from .forms import InstForm
from .models import InstModel
from .forms import LerForm
from .models import LerModel

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import *
from random import randrange
from django.core.mail import send_mail
import requests


def andy(request):
	if request.user.is_authenticated:
		data = AndyModel.objects.all()
		stu = { "andy": data }
		return render(request, "andy.html", stu)
	else:
		return redirect("ulogin")

def inst(request):
	if request.user.is_authenticated:
		data = InstModel.objects.all()
		stu = { "inst": data }
		return render(request, "inst.html", stu)
	else:
		return redirect("ulogin")


def ler(request):
	if request.user.is_authenticated:
		data = lerModel.objects.all()
		stu = { "ler": data }
		return render(request, "ler.html", stu)
	else:
		return redirect("ulogin")

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("andy")
	elif request.method =="POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un, password=pw)
		if usr is not None:
			login(request, usr)
			return redirect("andy")
		else:
			return render(request, "login.html", {"msg":"Invalid Username or Password"})
	else:
		return render(request, "login.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("andy")
	elif request.method =="POST":
		un = request.POST.get("un")
		try:
			usr = User.objects.get(username=un)
			return render(request, "signup.html", {"msg":"User Alreadly Registered "})
		except User.DoesNotExist:
			pw =""
			text = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			subject ="Welcome to Todo App Password Verification"
			text ="Ur password is " + str(pw)
			from_email ="aniket24aug22@gmail.com"
			to_email = [str(un)]
			send_mail(subject, text, from_email, to_email)
			usr = User.objects.create_user(username=un, password=pw)
			usr.save()
			return redirect("ulogin")
	else:
		return render(request, "signup.html")

def rnp(request):
	if request.method =="POST":
		un = request.POST.get("un")
		try:
			usr = User.objects.get(username=un)
			pw =""
			text = "123456789"
			for i in range(4):
				pw = pw + text[randrange(len(text))]
			print(pw)
			subject ="Welcome to TodoApp by Aniruddha"
			text ="Your login password is " + str(pw)
			from_email ="aniket24aug22@gmail.com"
			to_email = [str(un)]
			send_mail(subject, text, from_email, to_email)
			usr.set_password(pw)
			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist:
			return render(request, "rnp.html", {"msg":"user does not exists"})
	else:
		return render(request, "rnp.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")