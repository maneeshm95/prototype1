from django.shortcuts import render
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        signform = SignupForm(request.POST)
        if signform.is_valid():
            signform.save()

    else:
        signform = SignupForm()

    context = {
        'signform_key' : signform
    }
    return render(request, 'users/registration.html', context)
