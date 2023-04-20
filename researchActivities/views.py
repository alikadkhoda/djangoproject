from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

import accounts.views
from researchActivities.forms import searchForm
from researchActivities.models import Paper, Jozveh, Presentation



def paperListView(request) :
    SearchForm = searchForm(request.GET)
    if SearchForm.is_valid():
            searchText = SearchForm.cleaned_data["searchText"]
            papers = Paper.objects.filter(title__contains=searchText)
    else:
            papers = Paper.objects.all()

    context = {
        "papers": papers,
        "papersCount": papers.count(),
        "SearchForm": SearchForm,
    }
    return render(request, "researchActivities/papersList.html", context)
@login_required
def paperDetailsView(request, paper_id):
    # if request.user.is_authenticated and request.user.is_active:
        papers = Paper.objects.get(pk=paper_id)
        context = {
           "papers": papers,
        }
        return render(request, "researchActivities/paperDetails.html", context)
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))

@login_required
def jozvehListView(request):
    SearchForm = searchForm(request.GET)
    if SearchForm.is_valid():
        searchText = SearchForm.cleaned_data["searchText"]
        jozveh = Jozveh.objects.filter(title__contains=searchText)
    else:
        jozveh = Jozveh.objects.all()
    context = {
        "jozveh": jozveh,
        "SearchForm": SearchForm,
    }
    return render(request, "researchActivities/jozvehList.html", context)

@login_required
def presentationListView(request):
    SearchForm = searchForm(request.GET)
    if SearchForm.is_valid():
        searchText = SearchForm.cleaned_data["searchText"]
        present = Presentation.objects.filter(title__contains=searchText)
    else:
        present = Presentation.objects.all()
    context = {
        "presents": present,
        "SearchForm": SearchForm,
    }
    return render(request, "researchActivities/presentationList.html", context)

