# django_app/views.py

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.core.files.images import ImageFile
from django.contrib.auth.hashers import make_password

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            wow = Membership.objects.filter(user=current_user).last()
            if wow.role_name == 'user':
                return redirect('users_view')
            elif wow.role_name == 'surgeon':
                return redirect('surgeons_view')
            elif wow.role_name == 'radiologist':
                return redirect('radiologists_view')
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
        email = request.POST.get('email')
        role_name = request.POST.get('role_name')

        user_credential = UserCredential.objects.filter(username=username)
        if user_credential.exists():
            messages.error(request, "Username already exists. Please try a different username.")
            return redirect('register')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email = email,
        )
        user.save()
        hashed_password = make_password(password)
        cred = UserCredential.objects.create(
            user_id=user,
            username=username,
            password=hashed_password
        )
        cred.save()

        orgg = Organization.objects.create(
            org_owner=user,
            org_name = 'Test Organisation',
            org_description = 'Test Description',
            org_address = 'Test Address'
        )
        orgg.save()

        mem = Membership.objects.create(
            user_id=user,
            role_name=role_name,
            org_id=orgg
        )
        mem.save()

        messages.success(request, "Account created successfully.")
        return redirect('login_page')
    return render(request, 'register.html')



def user_view(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        new_image = UserImage(image=ImageFile(image_file))
        new_image.user = request.user
        new_image.save()
        messages.success(request, "Image uploaded")
        return redirect('success')
    return render(request, 'users_page.html')

