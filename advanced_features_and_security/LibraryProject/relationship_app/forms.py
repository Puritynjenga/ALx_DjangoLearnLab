from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form with additional fields."""
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.profile_photo = self.cleaned_data.get('profile_photo')
        if commit:
            user.save()
        return user
    
    