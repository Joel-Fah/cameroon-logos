from django.urls import path
from .views import HomeView

# My 'core' urls here
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
