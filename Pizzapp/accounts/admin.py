from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserChangeForm,MyUserCreationForm
from .models import MyUser
class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "tc_no",
        "phone_number",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
        "Other Info", 
            {"fields": (
                "tc_no",
                "phone_number",
                "card_no",
                "cv2",
                "exp_month",
                "exp_year",
            )}
        )   
    ,)
    add_fieldsets = UserAdmin.add_fieldsets
    readonly_fields = ['date_joined', 'last_login']
admin.site.register(MyUser, CustomUserAdmin)
