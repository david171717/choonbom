from django.shortcuts import render
from allauth.templates import account

def main(request):
	return render(request, 'home/main.html', {})

def test(request):
	return render(request, 'home/test.txt', {})

def logout(request):
	account.logout(reqeust)
	# return render(request, '/', {})
	return redirect('/')


def choosePartner(request):
	return render(request, 'home/choosePartner.html', {})

def choosePlace(request):
	return render(request, 'home/choosePlace.html', {})

def chooseFamily(request):
	return render(request, 'home/chooseFamily.html', {})

# Create your views here.
