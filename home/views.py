from django.shortcuts import get_object_or_404, render
from allauth.templates import account
from .models import Wedding
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.shortcuts import redirect



def main(request):
	return render(request, 'home/main.html', {})

def test(request):
	return render(request, 'home/test.txt', {})

def logout(request):
	account.logout(reqeust)
	# return render(request, '/', {})
	return redirect('/')


def myinfo(request, uid):

	user = User.objects.get(pk = uid)

	print("1")
	print(user)

	if Wedding.objects.filter(user_id = user).exists():
		wuser = Wedding.objects.get(user_id = user)
		print(wuser)

		print("2")
		# context = {'my_name' : wuser.my_name, 'my_gender' : wuser.my_gender}
		print("3")
		return render(request, 'home/myinfo.html', {})
		# return resolve_url('myinfo', user.id)

	else:
		print("4")
		wdata = Wedding(user_id = user)
		wdata.save()

		return render(request, 'home/myinfo.html', {})


def choosePartner(request, uid):
	print(uid)
	# 여기서 pk 로 넣어야해
	# wdata = Wedding.objects.filter(User.objects.filter(id=request.POST['id']))
	# wdata = get_object_or_404(User, pk=user_id)
	# print(wdata)
	# # wdata = Wedding.objects.all()
	# context = {'wdata' : wdata}
	# data = Wedding(user_id = user_id, my_name = request.POST['my_name'], my_gender =request.POST['my_gender'])
	# print(data)
	# data.save()


	user = User.objects.get(pk = uid)
	# if Wedding.objects.get(user_id = user).exists():
	# 	# context = {''}
	# else
	wdata = Wedding(user_id = user, my_name = request.POST['my_name'], my_gender =request.POST['my_gender'])
	wdata.save()

	return render(request, 'home/choosePartner.html', {})

def choosePlace(request):





	return render(request, 'home/choosePlace.html', {})

def chooseFamily(request):
	return render(request, 'home/chooseFamily.html', {})


# Create your views here.


