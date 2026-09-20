import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from finance.models import DashboardModule, NavigationItem

NavigationItem.objects.all().delete()
NavigationItem.objects.create(title='Dashboard', url='/', order=1)
NavigationItem.objects.create(title='Accounts', url='#', order=2)
NavigationItem.objects.create(title='Transactions', url='#', order=3)
NavigationItem.objects.create(title='Budgets', url='#', order=4)
NavigationItem.objects.create(title='Goals', url='#', order=5)
NavigationItem.objects.create(title='Subscriptions', url='#', order=6)

DashboardModule.objects.all().delete()
DashboardModule.objects.create(title='Total Balance', module_type='stat_balance', order=1)
DashboardModule.objects.create(title='Monthly Income', module_type='stat_income', order=2)
DashboardModule.objects.create(title='Monthly Expenses', module_type='stat_expense', order=3)
DashboardModule.objects.create(title='Income vs Expenses', module_type='chart_income_expense', order=4)
DashboardModule.objects.create(title='Spending by Category', module_type='chart_spending_category', order=5)
