from django.urls import path , include
from . import views 
from django.contrib.auth.views import LogoutView
app_name='application'
urlpatterns = [
    #ex : /survey/ =home
    
    path('',views.TaskList.as_view(),name='taskList'),
    path('task/<int:pk>/',views.TaskDetail.as_view(),name='detail'),
    path('task/create/',views.TaskCreate.as_view(),name='create'),
    path('task/update/<int:pk>/',views.TaskUpdate.as_view(),name="update"),
    path('task/history/',views.TaskHistory.as_view(),name='history'),
    path('task/delete/<int:pk>/',views.TaskDelete.as_view(),name="delete"),
    path('task/login/',views.TaskLogin.as_view(),name='login'),
    path('task/logout/',LogoutView.as_view(next_page='application:login'),name='logout')
    
    
   
    
]
