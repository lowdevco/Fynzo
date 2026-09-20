from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DashboardModule, Account
from .forms import AccountForm

# @login_required
def dashboard(request):
    modules = DashboardModule.objects.filter(is_active=True).prefetch_related('children')
    return render(request, 'pages/dashboard.html', {'modules': modules})

# @login_required
def account_list(request):
    # Fallback to a superuser if not logged in for testing
    user = request.user if request.user.is_authenticated else None
    
    accounts = Account.objects.all() if not user else Account.objects.filter(user=user)
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            if user:
                account.user = user
            else:
                # Assign to first user if testing without auth
                from accounts.models import User
                account.user = User.objects.first()
            account.save()
            messages.success(request, 'Account created successfully!')
            return redirect('account_list')
        else:
            messages.error(request, 'Error creating account. Please check the form.')
    else:
        form = AccountForm(initial={'currency': 'INR'})

    return render(request, 'pages/accounts.html', {'accounts': accounts, 'form': form})
