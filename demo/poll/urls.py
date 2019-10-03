from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='poll_list' ),
    path('<int:id>/details', detail, name='detail')
]