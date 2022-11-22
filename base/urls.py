from django.urls import path,include
from . import views

urlpatterns = [
   
    path('', views.all_task,name='all_task'),
    path('add-task/', views.add_task,name='add_task'),
    path('delete-task/', views.delete_task,name='delete_task'),
    path('mark-as-completed-task/', views.mark_task,name='mark_task'),
    path('completed-task/', views.complete_task,name='complete_task'),
]