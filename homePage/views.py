from django.shortcuts import render
from homePage.models import Biography,Favorites,Project
# Create your views here.
def indexView(request):
    context = {
        "biography":Biography.objects.all(),
        "favorites":Favorites.objects.all(),
        "projects":Project.objects.all()

    }
    return render(request, 'homPage/index.html', context)

def projectView(request):
    context ={
        "projects":Project.objects.all()
    }
    return render(request, 'homPage/project.html', context)