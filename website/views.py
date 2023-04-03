from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Logging.Logger_Base import log
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EmailForm


def home(request):
    # Check to see if login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            log.info(f'The user {username} has logged in')
            return redirect('home')
        else:
            messages.warning(request, 'There was an error logging in')
            log.warning(f'There was an error logging with the user {username}')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    log.info(f'The user has logged out')
    return redirect('home')


def mail(request):
    form = EmailForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                subject = request.POST['subject']
                message = request.POST['message']
                from_email = request.user.email
                to_email = [request.POST['email_to']]
                # send an email
                send_mail(
                    subject,  # subject
                    message,  # message
                    from_email,  # from email
                    to_email,  # to email
                )

                messages.success(request, 'Email Succesfully sent')
                return redirect('home')
        else:
            return render(request, 'mail.html', {
                'form': form,
                'email_from': request.user.email,
            })
    else:
        messages.warning(request, 'You need to be logged in')
        return redirect('home')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            messages.success(request, 'You have succesfully Logged In')
            log.info(
                f'The user {username} was created and logged in Succesfully')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})
