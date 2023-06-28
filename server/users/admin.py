from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'team_signup', 'has_consent', 'is_superuser')

admin.site.register(User, UserAdmin)