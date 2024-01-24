# views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.hashers import make_password
from .models import Receipe
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def receipes(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            
            print("Name:", name)
            print("Description:", description)
            
            # Process the form data or save it to the database
            Receipe.objects.create(
                user=request.user,
                name=name,
                description=description,
            )
            
        except MultiValueDictKeyError as e:
            print("Name:", request.POST.get('name'))
            print("Description:", request.POST.get('description'))
        
        return redirect('receipes')
    
    # Retrieve all recipes
    queryset = Receipe.objects.filter(user=request.user)  # Filter recipes by the current user
    context = {'receipes': queryset}
     
    return render(request, 'receipes.html', context)


def delete(request, id):
    try:
        queryset = Receipe.objects.get(id=id, user=request.user)  # Ensure the recipe belongs to the current user
        queryset.delete()
    except Receipe.DoesNotExist:
        messages.error(request, "Recipe not found.")
    
    return redirect('receipes')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('receipes')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request, "Username already exists. Please try a different username.")
            return redirect('register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully.")

        return redirect('login_page')
    
    return render(request, 'register.html')
