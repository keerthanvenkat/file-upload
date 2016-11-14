from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from .models import Address
from address.forms import ContactForm,AddressForm
import pdb

# Create your views here.

def hello_world(request):
	return HttpResponse("hello!! World ")

# def test_html(request):
# 	f = open('/home/key2gyaan/Documents/Technical/Django/Django_Projects/batch-5/src/address/templates/test1.html')
# 	content = f.read()
# 	return HttpResponse(content)


def test_html(request):
	context = {}
	return render(request,'test.html',context)

def test_html1(request):
	context = {}
	return render(request,'test1.html',context)

# admin one app.
# address is one app.

# def myaddress(request):
# 	context = {}
# 	return render(request,'address.html',context)

# def myaddress(request):
# 	context = {'name1':'student1','email1':'tuxfux.hlp@gmail.com','name2':'student2','email2':'tuxfux.hlp@edu.com'}
# 	return render(request,'address.html',context)
#
# def myaddress(request):
# 	context = {'namesdb':[{'name':'student1','email':'tuxfux.hlp@gmail.com'},{'name':'student2','email':'tuxfux.hlp@edu.com'}]}
# 	return render(request,'address.html',context)

def myaddress(request):
	values = Address.objects.all()
	print values
	context = {'namesdb': values}
	return render(request,'address.html',context)


def contact(request):
	form_class = ContactForm()  # Instance of the form class here.
	context = {'form':form_class}
	print dir(form_class)

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print dir(form)
			subject = "A new contact/lead"
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			content = form.cleaned_data['content']
			email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + content,
								 to=['tuxfux.hlp@gmail.com'])
			email.send()
		return HttpResponseRedirect('/thanks/')
	return render(request,'contact.html',context)

def address(request):
	form_class = AddressForm()
	context = {'form':form_class}

	print request.method
	if request.method == 'POST':
		form = AddressForm(request.POST)
		#print dir(form),form.is_valid(),type(form)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			age = form.cleaned_data['age']
			# form validation
			# TOMMORROW: we want to validate our code to work with mail which are edu.com
			# we also want the candidate to be above 18years and below 50 years.
			# then only we want to make a entry into the database.

			Address.objects.create(name=name,age=age,email=email)  # Making an entry into the database.
			return HttpResponseRedirect('/thanks/')
		else:
			print request.method,form
			context = {'form':form}
			return render(request,'address_forms.html',context)
	return render(request, 'address_forms.html', context)

	# homework : try to add the address model to to your admin as adminmodeforms and try to achieve the same in admin too.


def thanks(request):
	return HttpResponse("Thank you for submitting your details.")