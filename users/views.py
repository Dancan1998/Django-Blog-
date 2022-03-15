from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"Account created for ({username}) successfully")
            return redirect('blog:blog-home')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)
