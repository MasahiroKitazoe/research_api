from django import forms


class UserForm(forms.Form):
  user_id = forms.CharField()
  password = forms.CharField()
