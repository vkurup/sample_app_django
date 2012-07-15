import hashlib
from django import forms
from models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    password_confirmation = forms.CharField(label='Confirmation',
                                            widget=forms.PasswordInput,
                                            min_length=6)

    class Meta:
        model = User

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation:
            if password == password_confirmation:
                self.instance.password_digest = hashlib.sha256(password).hexdigest()
            else:
                raise forms.ValidationError('Password did not match confirmation')

        return cleaned_data
