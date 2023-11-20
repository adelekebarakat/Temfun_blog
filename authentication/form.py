from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from core.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','website_url','facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control',}),
            'website_url': forms.TextInput(attrs={'class': 'form-control',}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control',}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control',}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control',}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control',}),
            
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','website_url','facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control',}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control',}),
            'website_url': forms.TextInput(attrs={'class': 'form-control',}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control',}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control',}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control',}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control',}),
            
        }
        

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

 
  

        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
            
        }

    def clean_email(self):
    # Get the email
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class EditProfile(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
            
        }
