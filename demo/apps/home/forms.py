from django import forms

class contactForm(forms.Form):
	Email		=forms.EmailField(widget=forms.TextInput())
	Titulo		=forms.CharField(widget=forms.TextInput())
	Texto		=forms.CharField(widget=forms.Textarea())

class loginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput())
	password=forms.CharField(widget=forms.PasswordInput(render_value=False))
