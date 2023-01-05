from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('add_admin',views.add_admin, name='add_admin'),
    path('index_admin',views.index_admin, name='index_admin'),
    path('view_register',views.view_register, name='view_register'),
    path('add_department',views.add_department, name='add_department'),
    path('manage_department',views.manage_department, name='manage_department'),
    path('update/<int:idd>',views.update, name='update'),


]