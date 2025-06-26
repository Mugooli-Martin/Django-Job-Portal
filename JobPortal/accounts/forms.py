from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#Instead of - from django.contrib.auth.models import User
#Use the next two lines below, This way, User points to your custom model.
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput, PasswordInput

class JobseekerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']
        
    def save(self, commit=True ):
        user = super().save(commit=False)
        user.role = 'jobseeker'
        if commit:
            user.save()
        return user
class EmployerRegistrationForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employer'
        if commit:
            user.save()
        return user    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())
    
    
        