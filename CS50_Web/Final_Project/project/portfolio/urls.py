from django.urls import path
from . import views


urlpatterns = [
    path('', views.PortfolioView.as_view(), name="home"),
    path('add/', views.PortfolioAddView.as_view(), name="add_project")
]
