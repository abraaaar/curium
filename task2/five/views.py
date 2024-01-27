# django_app/views.py

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
import uuid

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['tab_id'] = str(uuid.uuid4())  # Generate a unique ID for this tab
            current_step = request.session.get('current_step', 'user_form_view')
            response = redirect(current_step)
            response.set_cookie('tab_id', request.session['tab_id'])  # Set the tab_id cookie
            return response
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, '1login.html')


def logout_page(request):
    if 'current_step' in request.session:
        del request.session['current_step']  # Clear current_step from session
    request.session.flush()
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

@login_required
def user_form_view(request):
    user_id = request.session.get('user_id')  # Get user ID from session
    tab_id = request.session.get('tab_id')  # Get tab ID from session

    # Check if user_id and tab_id exist and tab_id matches the tab_id stored when the user logged in
    if user_id is not None and tab_id is not None and tab_id == request.COOKIES.get('tab_id'):
        current_user = User.objects.get(id=user_id)
        if request.method == "POST":
            name = request.POST.get('name', 'Default Name')  # Provide a default name if not provided
            age = request.POST.get('age')
            gender = request.POST.get('gender')

            # Create a new UserProfile instance for each submission
            user_profile = UserProfile.objects.create(user=current_user, name=name, age=age, gender=gender)

            request.session['current_step'] = 'address_form_view'  # Store the current step in the session
            return redirect('address_form_view')
    else:
        return redirect('login_page')

    return render(request, '2name.html')

# def user_form_view(request):
#     user_id = request.session.get('user_id')  # Get user ID from session
#     if user_id is not None:
#         current_user = User.objects.get(id=user_id)
#         ...
#     else:
#         return redirect('login_page')
    
#     current_user = request.user
#     if request.method == "POST":
#         name = request.POST.get('name', 'Default Name')  # Provide a default name if not provided
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')

#         # Create a new UserProfile instance for each submission
#         user_profile = UserProfile.objects.create(user=current_user, name=name, age=age, gender=gender)

#         return redirect('address_form_view')

#     return render(request, '2name.html')


def address_form_view(request):
    if request.method == "POST":
        address = request.POST.get('address')
        
        user_profile = UserProfile.objects.last()
        user_profile.address = address
        user_profile.save()

        return redirect('edu_form_view')  
    
    return render(request, '3address.html')

def edu_form_view(request):
    if request.method == "POST":
        education = request.POST.get('education')
        
        user_profile = UserProfile.objects.last()
        user_profile.education = education
        user_profile.save()

        return redirect('interest_form_view') 
    
    return render(request, '4edu.html')

def interest_form_view(request):
    current_user = request.user
    if request.method == "POST":
        hobbies = request.POST.get('hobbies')

        # Get the latest UserProfile instance for the current user
        user_profile = UserProfile.objects.filter(user=current_user).last()
        user_profile.hobbies = hobbies
        user_profile.save()

        return redirect('user_details_view')

    return render(request, '5interest.html')

def user_details_view(request):
    if request.method == "POST":
        # Clearing user profile data
        user_profile = UserProfile.objects.filter(user=request.user).last()
        user_profile.save()

        # Redirect to the start of the form
        return redirect('user_form_view')

    # Retrieve all UserProfile entries for the current user
    user_data = UserProfile.objects.filter(user=request.user)

    # Pass the queryset to the template
    context = {'user_data': user_data}
    return render(request, 'user_details.html', context)




