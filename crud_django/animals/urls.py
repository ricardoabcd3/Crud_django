

from django.urls import path , include
from . import views

app_name='aplication'
urlpatterns = [
    #ex : /survey/ =home
    
    path('',views.animals,name='animals'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('create/',views.create,name='create'),
    path('delete/<int:id>/',views.delete,name='delete')
   
    
]
