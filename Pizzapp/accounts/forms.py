from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + (
            "phone_number",
            "tc_no",
            "card_no",
            "cv2",
            "exp_month",
            "exp_year",
            )
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields
