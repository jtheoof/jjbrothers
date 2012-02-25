from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def home(request):
	context = {}

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))


def weddings(request):
	context = {}

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))


def landscapes(request):
	context = {}

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))


def books(request):
	context = {}

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))

def about(request):
	context = {}

	return render_to_response(
	    'web/home.html',
	    context,
	    context_instance=RequestContext(request))

