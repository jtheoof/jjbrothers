from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = ContactForm()

    context = {
        'body_class': 'about',
        'form': form
    }
    return render_to_response(
        'web/contact.html',
        context,
        context_instance=RequestContext(request))

