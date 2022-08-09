from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import AccessRecord, Topic, UserProfileInfo, Webpage

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z!")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        exclude = ('user',)

class MyModelForm(forms.ModelForm):
    # Fields here
    class Meta:
        model = Webpage
        fields = '__all__'
        # fields = ("field1","field2")
        # exclude = ["field1","field2"]


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_data = super().clean()
        email = clean_data['email']
        verify_email = clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
