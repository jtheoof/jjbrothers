import os

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

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
        'web/home.html',
        context,
        context_instance=RequestContext(request))


def portfolios(request):
    context = { 'body_class': 'books' }

    return render_to_response(
        'web/portfolios.html',
        context,
        context_instance=RequestContext(request))

def contact(request):
    try:
        agent = request.META['HTTP_USER_AGENT']
    except:
        agent = None
    try:
        ip = request.META['REMOTE_ADDR']
    except:
        ip = os.environ['REMOTE_ADDR']
    akismet_api = Akismet(key=settings.AKISMET_API_KEY, agent=agent)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = {
                'user_ip': ip,
                'user_agent': agent,
                'comment_author_email': cd['sender'],
            }
            if akismet_api.comment_check(
                '%s - %s' % (cd['subject'], cd['message']),
                data):
                # Invalid (probably spam)
                pass
            else:
                return HttpResponseRedirect('/thanks')
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

