# Create your views here.
from django.http import HttpResponse

def index(request):
    """docstring for index"""
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    """Docstring para detail"""
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id ):
    """Docstring para results"""
    return HttpResponse("You're looking at the results of poll %s " % poll_id)

def vote(request, poll_id):
    """docstring for vote"""
    return HttpResponse("You're voting on poll %s" % poll_id)
