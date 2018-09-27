from django.urls import path
from .views import *
from .models import *

urlpatterns = [

    path('', IndexView.as_view(), name='Index')

]
