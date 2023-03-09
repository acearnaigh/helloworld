# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, resultsPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('results/', resultsPageView, name='results'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]


