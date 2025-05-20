from django.urls import path
from . import views

urlpatterns = [
    path("createbudget", views.createBudget, name="createbudget"),
]