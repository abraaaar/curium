from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from five.models import UserDetails, UserQualifications
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

NUM_STEPS = 5

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # Check for session variable indicating the last completed step
            last_step = request.session.get('last_step', 1)

            # If the user is trying to access the login page out of order, forbid the request
            if last_step != 1:
                return HttpResponseForbidden("Access Denied. Please follow the correct order.")

            return redirect('user_form_view') 
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, '1login.html')


@login_required
def logout_page(request):
    # Clear the session variable to reset the progress when the user logs out
    if 'last_completed_step' in request.session:
        del request.session['last_completed_step']
    logout(request)
    return redirect('login_page')

def register(request):
    # Check for session variable indicating the last completed step
    last_completed_step = request.session.get('last_completed_step', 1)

    # If the user is trying to access the registration page out of order, forbid the request
    if last_completed_step != 1:
        return HttpResponseForbidden("Access Denied. Please follow the correct order.")

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

        # Update the session variable for the last completed step
        last_completed_step = 2  # Assuming registration redirects to step 2
        request.session['last_completed_step'] = last_completed_step

        messages.success(request, "Account created successfully.")
        return redirect(f'{last_completed_step}name.html')
    
    return render(request, 'register.html')

@login_required
def user_form_view(request):
    current_user = request.user

    # Check for session variable indicating the last completed step
    last_step = request.session.get('last_step', 1)

    if request.method == "POST":
        name = request.POST.get('name', 'Default Name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        user_details = UserDetails.objects.create(user=current_user, name=name, age=age, gender=gender)

        # Update the session variable for the last completed step
        last_step += 1
        request.session['last_step'] = last_step

        # Redirect to the next step if available, else redirect to the final page
        if last_step <= NUM_STEPS:
            return redirect(f'{last_step}address.html' if last_step == 1 else 'user_details_view')
        else:
            # Reset the session variable to 1 for a new cycle if needed
            request.session['last_step'] = 1
            return redirect('user_details_view')

    print(last_step)
    return render(request, f'{last_step}name.html')


@login_required
def address_form_view(request):
    current_user = request.user

    # Check for session variable indicating the last completed step
    last_step = request.session.get('last_step', 1)

    if request.method == "POST":
        address = request.POST.get('address')
        user_qualifications = UserQualifications.objects.create(user=request.user, address=address)

        # Update the session variable for the last completed step
        last_step += 1
        request.session['last_step'] = last_step

        # Redirect to the next step if available, else redirect to the user_details_view
        if last_step <= NUM_STEPS:
            return redirect(f'{last_step}edu.html' if last_step == 1 else 'user_details_view')
        else:
            # Reset the session variable to 1 for a new cycle if needed
            request.session['last_step'] = 1
            return redirect('user_details_view')

    return render(request, f'{last_step}address.html')

@login_required
def edu_form_view(request):
    current_user = request.user

    # Check for session variable indicating the last completed step
    last_step = request.session.get('last_step', 1)

    if request.method == "POST":
        education = request.POST.get('education')
        user_qualifications = UserQualifications.objects.filter(user=request.user).last()
        user_qualifications.education = education
        user_qualifications.save()

        # Update the session variable for the last completed step
        last_step += 1
        request.session['last_step'] = last_step

        # Redirect to the next step if available, else redirect to the final page
        if last_step <= NUM_STEPS:
            return redirect(f'{last_step}interest.html' if last_step == 1 else 'user_details_view')
        else:
            # Reset the session variable to 1 for a new cycle if needed
            request.session['last_step'] = 1
            return redirect('user_details_view')

    return render(request, f'{last_step}edu.html')


@login_required
def interest_form_view(request):
    current_user = request.user

    # Check for session variable indicating the last completed step
    last_step = request.session.get('last_step', 1)

    if request.method == "POST":
        hobbies = request.POST.get('hobbies')
        user_qualifications = UserQualifications.objects.filter(user=request.user).last()
        user_qualifications.hobbies = hobbies
        user_qualifications.save()

        # Update the session variable for the last completed step
        last_step += 1
        request.session['last_step'] = last_step

        # Redirect to the next step if available, else redirect to the final page
        if last_step <= NUM_STEPS:
            return redirect('user_details_view')
        else:
            # Reset the session variable to 1 for a new cycle if needed
            request.session['last_step'] = 1
            return redirect('user_details_view')

    return render(request, f'{last_step}interest.html')

@login_required
def user_details_view(request):
    current_user = request.user

    # Check for session variable indicating the last completed step
    last_step = request.session.get('last_step', 1)

    if request.method == "POST":
        # Reset the session variable to 1 for a new cycle
        request.session['last_step'] = 1
        return redirect('user_form_view')

    user_details = UserDetails.objects.filter(user=current_user)
    user_qualifications = UserQualifications.objects.filter(user=current_user)
    context = {
        'user_details': user_details,
        'user_qualifications': user_qualifications,
    }

    return render(request, f'user_details{last_step}.html', context)
