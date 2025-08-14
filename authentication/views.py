
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import User 


def signupPage(request):
    context = {
        "error": ""
    }
    if request.method == "POST":
      
        user_check = User.objects.filter(username=request.POST['username'])
        if user_check.exists():
            context["error"] = "Username already exists!"
            return render(request, 'signup.html', context)
        
 
        new_user = User(
            username=request.POST['username'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()

       
        return redirect('/')

    return render(request, 'signup.html', context)



def loginpage(request): 
    context = {"error": ""}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

       
        if username == "admin" and password == "admin123":
            return redirect('adminpage/')  
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home/') 
        else:
            context["error"] = "Invalid username or password"

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')
def home(request):
    return render(request, 'home.html')
def adminpage(request):
    return render(request, 'admin.html')


