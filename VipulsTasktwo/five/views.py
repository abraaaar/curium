from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from five.models import UserDetails, UserQualifications
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_form_view') 
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, '1login.html')
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
def user_form_view(request):
    current_user = request.user
    if request.method == "POST":
        name = request.POST.get('name', 'Default Name') 
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        user_details = UserDetails.objects.create(user=current_user, name=name, age=age, gender=gender)
        return redirect('address_form_view')
    return render(request, '2name.html')
def address_form_view(request):
    if request.method == "POST":
        address = request.POST.get('address')
        user_qualifications = UserQualifications.objects.create(user=request.user, address=address)
        return redirect('edu_form_view')  
    return render(request, '3address.html')
def edu_form_view(request):
    if request.method == "POST":
        education = request.POST.get('education')
        user_qualifications = UserQualifications.objects.filter(user=request.user).last()
        user_qualifications.education = education
        user_qualifications.save()
        return redirect('interest_form_view') 
    return render(request, '4edu.html')
def interest_form_view(request):
    if request.method == "POST":
        hobbies = request.POST.get('hobbies')
        user_qualifications = UserQualifications.objects.filter(user=request.user).last()
        user_qualifications.hobbies = hobbies
        user_qualifications.save()

        return redirect('user_details_view') 

    return render(request, '5interest.html')
def user_details_view(request):
    if request.method == "POST":
        return redirect('user_form_view')
    user_details = UserDetails.objects.filter(user=request.user)
    user_qualifications = UserQualifications.objects.filter(user=request.user)
    context = {
        'user_details': user_details,
        'user_qualifications': user_qualifications,
    }
    return render(request, 'user_details.html', context)
