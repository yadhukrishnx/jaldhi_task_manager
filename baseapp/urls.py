from django.urls import path
from . import views

urlpatterns = [
   path("base/",views.index,name="home"),
   path("",views.addtask,name="addtask"),
   path("listtask",views.listtask,name="listtask"),
   path("completedtask",views.completedtask,name="completedtask"),
   path("task/<int:pk>/",views.taskdetails,name="taskdetails"),
   path("completetask/<int:pk>/",views.completetask,name="completetask"),
]
