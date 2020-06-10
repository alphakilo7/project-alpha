from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
	if req.GET.get("page") == "login":
		return render(req, "sqlite/login.html")
	elif req.GET.get("page") == "register":
		return render(req, "sqlite/register.html")
	elif req.GET.get("page") == "reg":
		fname = req.POST.get("first_name")
		lname = req.POST.get("last_name")
		email = req.POST.get("email_addr")
		uname = req.POST.get("username")
		pword = req.POST.get("password")

		meta = {
			'fname': fname,
			'lname': lname,
			'email': email,
			'uname': uname,
			'pword': pword,
		}
		for k, v in meta.items():
			print(f">>> {k} -> {v}")
		return render(req, "sqlite/login.html")
	else:
		return render(req, "sqlite/index.html")
