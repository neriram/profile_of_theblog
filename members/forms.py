from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'pintrest_url', 'twitter_url') 

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}) , 
            #'profile_pic': , 
            'website_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}), 
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}) , 
            'pintrest_url':forms.TextInput(attrs={'class': 'form-control'}), 
            'twitter_url':forms.TextInput(attrs={'class': 'form-control'})
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')