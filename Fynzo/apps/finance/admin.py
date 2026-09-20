from django.contrib import admin
from .models import Account, Category, Transaction, Budget, Goal, Subscription, NavigationItem, DashboardModule

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Goal)
admin.site.register(Subscription)

@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(DashboardModule)
class DashboardModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'module_type', 'parent', 'order', 'is_active')
    list_editable = ('order', 'is_active')
