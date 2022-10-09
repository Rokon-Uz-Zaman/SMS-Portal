from django.shortcuts import render ,HttpResponse
import requests
from django.http import HttpResponse
from message.models import Contact
from message.forms import MessageForm,GMessageForm,ContactForm,GContactForm

# Create your views here.


def message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = MessageForm(request.POST)		
	
	return render(request,'message.html',{'form':form})

def gmessage(request):
	if request.method == 'POST':
		form = GMessageForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = GMessageForm(request.POST)
	
	return render(request,'gmessage.html',{'form':form})



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = ContactForm(request.POST)
	
	return render(request,'contact.html',{'form':form})


def gcontact(request):
	if request.method == 'POST':
		form = GContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = GContactForm(request.POST)
	
	return render(request,'gcontact.html',{'form':form})


def fromExcel(request):
	
	return render(request,'fromexcel.html')

def signIn(request):
	
	return render(request,'login.html')

def reports(request):
	
	return render(request,'reports.html')







#create contact
def createcontact(request):
	pass




def sendSMS():
	api_key =0
	msg=0
	num=0
	url=f'https:api.sms.net.bd/sendsms?api_key={api_key}&msg={msg}&to={num}'
	success_msg='<h2> Your message was send </h2>'
	return HttpResponse(sucess_msg)
