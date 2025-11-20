from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    """
    Simple home view. Replace 'home.html' with your actual template.
    """
    try:
        return render(request, "home.html")
    except Exception:
        # Fallback if template missing
        return HttpResponse("<h1>Home</h1><p>Replace templates/home.html with your template.</p>")


def about(request):
    try:
        return render(request, "about.html")
    except Exception:
        return HttpResponse("<h1>About</h1><p>Replace templates/about.html with your template.</p>")


def contact(request):
    try:
        return render(request, "contact.html")
    except Exception:
        return HttpResponse("<h1>Contact</h1><p>Replace templates/contact.html with your template.</p>")


def login_view(request):
    """
    Basic login view. If your project already has forms/auth logic, replace this.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("customerportal:dashboard")
        messages.error(request, "Invalid username or password")
        return redirect("login")

    # GET
    try:
        return render(request, "login.html")
    except Exception:
        # fallback
        html = """
        <h1>Login</h1>
        <form method="post">
            <input name="username" placeholder="username" required><br>
            <input name="password" type="password" placeholder="password" required><br>
            <button type="submit">Login</button>
        </form>
        """
        return HttpResponse(html)


def logout_view(request):
    auth_logout(request)
    return redirect("login")
