from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from trailheadlane.tasks import test_tasks

from thisishill.loggers import logger


def about(request, td=None):
    """
    Render Trailhead Lane Project About Page
    """
    logger.info("Accessing Trailhead Lane About...")
    return render(request, "trailheadlane/about.html", td)


def trader(request, td=None):
    """
    Render Trailhead Lane Project Trader Page
    """
    logger.info("Accessing Trailhead Lane Trader...")
    return render(request, "trailheadlane/trader.html", td)


def analyzer(request, td=None):
    """
    Render Trailhead Lane Project Analyzer Page
    """
    logger.info("Accessing Trailhead Lane Analyzer...")
    return render(request, "trailheadlane/trader.html", td)
