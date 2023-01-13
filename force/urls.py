from django.urls import path
from.import views
urlpatterns=[
    path('',views.pro),
    path('login',views.login),
    path('register',views.reg)
]