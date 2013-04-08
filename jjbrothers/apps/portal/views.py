# -*- coding=utf-8
import os

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from akismet import Akismet
from forms import ContactForm

def home(request):
    context = { 'body_class': 'home' }
    return render_to_response(
        'web/home.html',
        context,
        context_instance=RequestContext(request))

def weddings(request):
    context = { 'body_class': 'weddings' }
    return render_to_response(
        'web/weddings.html',
        context,
        context_instance=RequestContext(request))

def landscapes(request):
    context = { 'body_class': 'landscapes' }
    return render_to_response(
        'web/landscapes.html',
        context,
        context_instance=RequestContext(request))


def portfolios(request):
    context = { 'body_class': 'books' }
    return render_to_response(
        'web/portfolios.html',
        context,
        context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if check_contact_form(request, cd): # This is spam
                m = _(u"Erreur lors de l'envoi réessayer ultérieurement.")
                messages.add_message(request, messages.ERROR, m)
            else:
                for m in [
                    _(u'Merci de nous avoir contactés.'),
                    _(u'Nous vous répondrons très rapidement.'),]:
                    messages.add_message(request, messages.INFO, m)
                message = '%s\r\n' % cd['message']
                message += 'From:  %s\r\n' % cd['sender']
                message += 'Email: %s\r\n' % cd['email']
                send_mail(
                    cd['subject'].encode("utf-8"),
                    message.encode("utf-8"),
                    settings.SERVER_EMAIL,
                    ['johan@jjbrothers.net', 'jeremy@jjbrothers.net'])
            return HttpResponseRedirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Formulaire invalide.')
    else:
        form = ContactForm(label_suffix='')

    context = {
        'body_class': 'about',
        'form': form
    }
    return render_to_response(
        'web/contact.html',
        context,
        context_instance=RequestContext(request))

def check_contact_form(request, cd):
    agent = request.META.get('HTTP_USER_AGENT', '')
    ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    akismet_api = Akismet(key=settings.AKISMET_API_KEY)
    data = {
        'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
        'referrer': request.META.get('HTTP_REFERER', ''),
        'comment_author': cd['sender'],
        'comment_author_email': cd['email'],
    }
    mes = '%s - %s' % (cd['subject'], cd['message'])
    return akismet_api.comment_check(mes.encode("utf-8"), data)

