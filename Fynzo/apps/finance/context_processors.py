from .models import NavigationItem

def navigation(request):
    return {
        'nav_items': NavigationItem.objects.filter(parent__isnull=True, is_active=True).prefetch_related('children')
    }
