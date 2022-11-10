from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=(('', '--Selecione uma opção--'), ('male', 'Homem'), ('female', 'Mulher')),
                               label='Gênero', required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Data de nascimento', required=True,
                                 widget=forms.DateInput(attrs={'data-target': '#datetimepicker1', 'class': 'form-control'})),
    first_name = forms.CharField(max_length=150, label='Nome', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, label='Sobrenome', required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=255, label='Senha', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=255, label='Confirmação de senha', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "gender", "birth_date", "email")
        labels = {
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "gender": "Gênero",
            "birth_date": "Data de Nascimento",
            "email": "Email"
        }

    def save(self, commit=True):
        try:
            print(self)
            user = super(NewUserForm, self).save(commit=False)
            print(self.cleaned_data)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.gender = self.cleaned_data['gender']
            user.birth_date = self.cleaned_data['birth_date']
        except Exception as e:
            print(e)
            messages = e
            return messages
        if commit:
            user.save()
        return user
