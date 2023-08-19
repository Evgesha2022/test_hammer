from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from auth_user.models import Enter, Code, Profile
from phonenumber_field.modelfields import PhoneNumberField
class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Enter
        fields = [ 'phone_number']
class UserCodeForm(forms.ModelForm):
    class Meta:
        model =Code
        fields=['code']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['inv_code_fr']  # Укажите поля, которые вы хотите вводить
