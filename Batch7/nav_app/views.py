from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nav(req):
	return HttpResponse("<style>h1{text-align:center;background-color:aqua;}</style><h1>Welcome to home page</h1><h2 style='color:black;background-color:Gold;'>Naveen</h2>")
def ch(req):
	return HttpResponse("<script>alert('click ok to display MSG')</script><h2>welcome</h2>")
def home(req):
	return render(req,'navtemp/home.html')

def lg(req):
	return render(req,'navtemp/login.html')
def reg(req):
	return render(req,'navtemp/register.html')
def bthm(req):
	return render(req,'navtemp/bthm.html')
def about(req):
	return render(req,'navtemp/about.html')
def contact(req):
	return render(req,'navtemp/contact.html')