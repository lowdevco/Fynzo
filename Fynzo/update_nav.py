import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from finance.models import NavigationItem

acc = NavigationItem.objects.filter(title='Accounts', parent__isnull=True).first()
if acc:
    acc.url = '/accounts/'
    acc.save()
