from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from validate_email import validate_email


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # email = request.POST.get('email')
        # is_valid = validate_email(email)
        # print(email)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"account has been created successfully for {username}")
            return redirect('users:user-login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)


@login_required(login_url='users:user-login')
def profile(request):
    return render(request, 'users/profile.html')
