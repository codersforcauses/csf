from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.pk is not None:  # Existing user
            original_obj = self.model.objects.get(pk=obj.pk)
            if obj.password == original_obj.password:
                # Password hasn't changed, no need to rehash
                obj.password = original_obj.password
            else:
                # Password has changed, rehash the new password
                obj.set_password(obj.password)
        else:
            # New user, hash the password
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)

    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'team_signup', 'has_consent', 'is_superuser')


admin.site.register(User, UserAdmin)
