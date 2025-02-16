from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model =CustomerUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age',)}),
    )


admin.site.register(CustomerUser, CustomerUserAdmin)

