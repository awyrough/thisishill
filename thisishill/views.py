import re

# from django.http import HttpResponse
# from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate


from thisishill.loggers import logger


def landing(request):
    """
    Render landing page at www.hillwyrough.com/
    """
    td = {}
    return render(request, "thisishill/landing.html", td)


def sign_in(request):
    """
    Sign in to private projects.
    """

    def _is_email(email):
        """
        Return True if acceptable email format, False if not.
        """
        VALID_REGEX_EMAIL = r"[^@]+@[^@]+\.[^@]+"
        email_pattern = re.compile(VALID_REGEX_EMAIL)
        if email_pattern.match(email):
            return True
        else:
            return False

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if _is_email(username):
            try:
                user_from_email = User.objects.get(email=username)
                username = user_from_email.username
            except User.DoesNotExist:
                logger.error("Invalid login from email: %s", username)
                messages.error(request, "Hill can't find an account with that email address.")
                return render(request, "sign_in.html")
        else:
            if not User.objects.filter(username=username).exists():
                logger.error("Invalid login from username: %s", username)
                messages.error(request, "Hill can't find an account with that username.")
                return render(request, "sign_in.html")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                redirect_url = request.GET.get("next", "/")
                return redirect(redirect_url)
            else:
                logger.error("Disabled account tried to log in, ID: %s", user)
                messages.error(
                    request, "Account disabled. Please email alexander.hill.wyrough@gmail.com for more information.")
                return render(request, "sign_in.html")
        else:
            logger.error("Invalid login from username: %s", username)
            messages.error(request, "Invalid login. Please try again.")
            return render(request, "sign_in.html")
    else:
        return render(request, "sign_in.html")


def sign_out(request):
    """
    Sign out from private projects.
    """
    auth_logout(request)
    return redirect("/")
