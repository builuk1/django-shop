from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# from .views import HomePageView
#
# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
# ]