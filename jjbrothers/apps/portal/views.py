from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

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


def books(request):
	context = { 'body_class': 'books' }

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))

def about(request):
	context = { 'body_class': 'about' }

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))

