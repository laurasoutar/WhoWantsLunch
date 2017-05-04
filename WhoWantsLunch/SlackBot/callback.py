from django.http import HttpResponse

def process( request ):
	return HttpResponse( "TESTING" )