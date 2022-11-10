from django.shortcuts import render, redirect
from .forms import NewIssueForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Issue


def home(request):
    issues = Issue.objects.all()
    return render(request, "help_support/home.html", {
        "issues": issues
    })

@login_required(login_url='/accounts/signin/?next=/issues/create/')
def create_issue(request):
    if request.method == "POST":
        form = NewIssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=True)
            messages.success(request, f"Issue {issue.title} reported successfully!")
            return redirect("home")
        messages.error(request, "Invalid information.")
    form = NewIssueForm()
    return render(request, "help_support/issue_form.html", context={"form":form})
