from django.shortcuts import render

def main(request):
	return render(request, 'home/main.html', {})

def test(request):
	return render(request, 'home/test.txt', {})

# Create your views here.
