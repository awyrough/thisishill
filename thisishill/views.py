from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def landing(request):
    """
    Render landing page at www.hillwyrough.com/
    """
    td = {}
    return render(request, "thisishill/landing.html", td)