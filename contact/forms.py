from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 200)
	company = forms.CharField(max_length = 300)
	email = forms.EmailField()
	contact_no = forms.IntegerField()
	project_name = forms.CharField(max_length = 200)
	project_info = forms.CharField(max_length = 1000,widget=forms.Textarea)