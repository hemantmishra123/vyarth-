from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myapp.models import SubmitWaste,CollectWaste
import django.contrib.sites

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class SubmitWasteForm(forms.ModelForm):
    class Meta:
        model= SubmitWaste
        fields = ['contact','number','communityName','typeofwaste','quantityofwaste','email','address']

class CollectWasteForm(forms.ModelForm):

    class Meta:
        model= CollectWaste
        fields = ['email']
