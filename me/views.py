from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from trailheadlane.tasks import test_tasks

from thisishill.loggers import logger


def me(request, td=None):
    """
    Render main site page at www.hillwyrough.com/me
    """
    logger.info("Accesing me page...")

    task = test_tasks()

    td = {
        "result": task.result,
    }
    return render(request, "me/me.html", td)


def d3_resume(request, td=None):
    """
    Display interactive d3 built resume
    """
    logger.info("Accessing d3r3sum3...")
    return render(request, "me/d3r3sum3.html", td)
