from django.shortcuts import render
from django.http import HttpResponse
from .models import Address
from address.forms import ContactForm,AddressForm
from django.core.mail import EmailMessage
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
# request (url) -> view(function) -> reponse(url)

def hello_world(request):
	return HttpResponse('hello world!!!')

def thanks(request):
	return HttpResponse("thanks you for contacting us")

def aboutus(request):
    context={}
    return render(request,'address/about.html',context)

# def test_html(request):
# 	f = open("/home/learn-django/Documents/Addressbook/src/address/templates/test.html")
# 	content=f.read()
# 	return HttpResponse(content)

def test_html(request):
	context={}
	return render(request,'address/test.html',context)

def myhome(request):
    context={}
    return render(request,'home.html',context)

# def address_html(request):
# 	context={}
# 	return render(request,'address.html',context)

# def address_html(request):
# 	context={'name1':'student1','name2':'student2','email1':'student1@edu.com','email2':'student2@edu.com'}
# 	return render(request,'address.html',context)

# def address_html(request):
# 	context={'namesdb':[{'name':'stu1','email':'stu@edu.com'},{'name':'stu2','email':'stu2@edu.com'}]}
# 	return render(request,'address.html',context)

def address_html(request):
	value=Address.objects.all()
	print value
	context={'namesdb':value}
	return render(request,'address.html',context)

def contact(request):
    form_class = ContactForm  # instance of the contact form.
    print form_class
    context={'form':form_class}

    if request.method == 'POST':
    	form = ContactForm(request.POST)
    	
    	if form.is_valid():
    		print dir(form)

    		contact_email = form.cleaned_data['contact_email']
    		contact_name  = form.cleaned_data['contact_name']
    		content = form.cleaned_data['content']
    		subject = " one more lead for - django {}".format(contact_email)
    		email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + content , to=['tuxfux.hlp@gmail.com'])
    		email.send()
    	return HttpResponseRedirect('/thanks/')
    return render(request,'contact_form.html',context)


def  address(request):
    form_class = AddressForm  # instance of the contact form.
    context={'form':form_class}

    if request.method == 'POST':
    	form = AddressForm(request.POST)
    	
    	if form.is_valid():
    		print dir(form)
    		name = form.cleaned_data['name']
    		email  = form.cleaned_data['email']
    		age = form.cleaned_data['age']
    		print name,email,age
    	return HttpResponseRedirect('/thanks/')
    return render(request,'address/address_form.html',context)



