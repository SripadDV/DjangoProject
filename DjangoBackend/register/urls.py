from django.urls import path

from . import views
from . import views2

urlpatterns = [
    path('',views2.register),
    path('reg', views.reg)
]