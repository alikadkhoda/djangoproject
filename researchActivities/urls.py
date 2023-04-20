from django.urls import path
from researchActivities import views

urlpatterns = [
path('papers/list', views.paperListView),
path('papers/list/<int:paper_id>', views.paperDetailsView),
path('jozveh/list', views.jozvehListView),
path('presentations/list', views.presentationListView)
]
