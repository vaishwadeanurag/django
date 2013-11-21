from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ContactForm
from contact.models import Contact

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			company = form.cleaned_data['company']
			email = form.cleaned_data['email']
			contact_no = form.cleaned_data['contact_no']
			project_name = form.cleaned_data['project_name']
			project_info = form.cleaned_data['project_info']

			new_contact = Contact(name = name,company =company,email=email,contact_no=contact_no,project_name=project_name,project_info=project_info)
			new_contact.save()
			return HttpResponseRedirect('/thanks')
	else:
		form = ContactForm()

	return render(request,'contact.html',{'form':form})

def thanks(request):
	return render(request,'thanks.html')

