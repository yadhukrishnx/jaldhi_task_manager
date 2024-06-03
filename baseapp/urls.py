from django.urls import path
from . import views

urlpatterns = [
   path("base/",views.index,name="home"),
   path("addtask",views.addtask,name="addtask"),
   path('search/', views.searchtask, name='searchtask'), 
   path("listtask",views.listtask,name="listtask"),
   path("completedtask",views.completedtask,name="completedtask"),
   path("task/<int:pk>/",views.taskdetails,name="taskdetails"),
   path("completetask/<int:pk>/",views.completetask,name="completetask"),
   path("deletetask/<int:pk>/",views.deletetask,name="deletetask"),
   path("confirmdelete/<int:pk>/",views.confirmdelete,name="confirmdelete"),
   path("register/",views.register,name="register"),
   path("",views.login,name="login"),
   path("logout/",views.logout,name="logout"),
   path("profile/",views.profile,name="profile"),
   path('profile/edit/', views.editprofile, name='editprofile'),
   

]
