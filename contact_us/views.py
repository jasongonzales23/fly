from django.conf.urls.defaults import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from contact_us.models import ContactForm
from django.core.context_processors import csrf
from django.core import mail
import models

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']            
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            interest = form.cleaned_data['interest']
            subject = 'Thanks for your interest in FLY Aviation'
            message = 'Hi ' + first_name + ', \nThanks for contacting us! \nThis email isn\'t from an actual human, I am just some software. My only job is to let you know that one of our experienced staff (a human!) will be contacting you very soon. Be very excited, FLY is awesome. \nCheers!\nThe FLY-Bot'
            sender = 'info@flyaviationgroup.com'
            recipients = [ email ]
        
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients, fail_silently=False)
            new_contact = form.save()

            #also send notifications to staff
            staff_subject = 'Contact from FLY Website'
            staff_message = 'Here is the info:\nName: ' + first_name + ' ' + last_name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nInterested in:' + interest
            staff_recipients = [ 'jason.gonzales23@gmail.com', 'Alex.Roush@flyaviationgroup.com']
            send_mail(staff_subject, staff_message, sender, staff_recipients, fail_silently=False)
            
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
        
    return render_to_response('contact.html',
        {'form': form,},
        context_instance=RequestContext(request)
    )
