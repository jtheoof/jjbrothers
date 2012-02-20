from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context = {}

	return render_to_response('web/home.html', context)

def weddings(request):
	context = {}

	return render_to_response('web/weddings.html', context)