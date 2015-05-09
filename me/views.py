from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from trailheadlane.tasks import test_tasks

from thisishill.loggers import logger

def me(request):
    """
    Render main site page at www.hillwyrough.com/me
    """
    logger.info("Accesing main view...")

    task = test_tasks()

    td = {
        "result": task.result,
    }
    return render(request, "me/me.html", td) 