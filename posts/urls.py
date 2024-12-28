from django.urls import path
from .views import HomePageView,MorePageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("more/", MorePageView.as_view(), name='more'),
]