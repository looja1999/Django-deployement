from django.contrib.auth.models import User
from django import forms 
from basicapp.models import UserProfileIno

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInoForm(forms.ModelForm):
    class Meta:
        model = UserProfileIno
        fields = ('profile_pic', 'portfolio_url')
