from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def me(request):
    """
    Render main site page at www.hillwyrough.com/me
    """
    td = {}
    return render(request, "me/me.html", td) 