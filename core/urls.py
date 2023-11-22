from django.urls import path
from .views import HomeView, AddLogoView

# My 'core' urls here
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddLogoView.as_view(), name='add_logo'),
]
