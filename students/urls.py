from django.urls import path
from . import views


urlpatterns = [
    path('register_students',views.register_students, name='register_students'),
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('after_login',views.after_login, name='after_login'),
    
]