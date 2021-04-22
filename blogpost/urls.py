from django.urls import path
from .views import BlogList

urlpatterns = [
    path('', BlogList.as_view()),
    path('list/', BlogList.as_view())
]