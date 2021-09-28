from django import forms

class ContactForm(forms.Form):
  form_class = {"class":"form-control"}

  name = forms.CharField(max_length=200,required=True,widget=forms.TextInput(form_class))
  email = forms.EmailField(required=True,widget=forms.TextInput({"class":"form-control","type":"email"}))
  subject = forms.CharField(max_length=200,required=True,widget=forms.TextInput(form_class))
  message = forms.CharField(required=True,widget=forms.Textarea(attrs=form_class))