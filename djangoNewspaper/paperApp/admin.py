from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomModel
    list_display=['email', 'username', 'age', 'is_staff', ] 


admin.site.register(CustomModel, CustomUserAdmin)
