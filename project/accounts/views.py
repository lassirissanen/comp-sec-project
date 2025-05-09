from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            # Redirect to homepage or another page
            return redirect('securityforum:home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
