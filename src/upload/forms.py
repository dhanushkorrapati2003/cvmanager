from django import forms
from .models import Person, CustomUser
from phonenumber_field.formfields import PhoneNumberField

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'resume' , 'skills']
    


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)
    query_type = forms.ChoiceField(label='Field Type', choices=[('first_name', 'First Name'), ('last_name', 'Last Name'), ('phone_number', 'Phone Number'), ('email', 'Email'), ('skills', 'Skills')], required=False)

class AuditLogSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)
    query_type = forms.ChoiceField(label='Field Type', choices=[('username', 'Username'), ('action', 'Action'), ('timestamp', 'Timestamp'), ('before', 'Before'), ('after', 'After')], required=False)
    
class AdminNewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password', 'is_superuser')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')


        