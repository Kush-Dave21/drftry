from django.urls import path, include
from appmate.api.views import *

urlpatterns = [
    path('list/',WatchListAV.as_view(), name='list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-lists'),
]