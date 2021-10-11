from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request,'invalid credentials.')
      return redirect('login')

  else:
    return render(request,'login.html')


def register(request):

  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    email = request.POST['email']

    if password == password2:
      if User.objects.filter(username=username).exists():
        print('Username taken')
        messages.info(request,'Username Already Taken')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        print('Email taken.')
        messages.info(request,'Email Already Taken')
        return redirect('register')


      else: 
        user = User.objects.create_user(username = username,password = password, email=email,first_name = first_name, last_name = last_name)
        user.save()
        print('User Created.')
        return redirect('login')

    else: 
      print('Password not matching.')
      messages.info(request,'Password doesnot match')
      return redirect('register')

    return redirect('/')
  else:
    return render(request,'register.html')

def logout(request):
  auth.logout(request)
  return redirect('/')
