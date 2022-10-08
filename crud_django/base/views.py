from urllib import response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.
class TaskList(ListView):
    '''Show home page'''
    model=Task
    #to change the default variable 
    context_object_name= 'tasks'
    def get_queryset(self):
        return Task.objects.filter(complete=False)
class TaskHistory(ListView):
    model=Task
    context_object_name= 'history'
    template_name='base/history.html'
    def get_queryset(self):
        '''this function show all items which have been completed'''
        return Task.objects.filter(complete=True)
    
class TaskDetail(DetailView):
    model= Task
    context_object_name='task'
    #to modify default template name
    template_name='base/task.html'
class TaskCreate(CreateView):
    model=Task
    fields=['user','title','description',]
    success_url= reverse_lazy('application:taskList')    
    template_name='base/create.html'
class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    template_name='base/task_update.html'
    success_url= reverse_lazy('application:taskList')  
class TaskDelete(DeleteView):
    model=Task    
    template_name='base/task_delete.html'
    success_url= reverse_lazy('application:history')  

class TaskLogin(LoginView):
    template_name: str='base/login.html'
    fields='__all__'
    redirect_authenticated_user: bool=True
    def get_success_url(self) -> str:
        return reverse_lazy('application:taskList')
     
class TaskLogout(LogoutView):
    template_name: str='base/logout.html'
    fields='__all__'
    redirect_authenticated_user: bool=True
    def get_success_url(self) -> str:
        return reverse_lazy('application:taskList')
    context_object_name='task' 

# def handler404(request,*args,**argv):
#     response=render_to_response('404.html',{},context_instance=RequestContext(request))
#     response.status_code=404
#     return response

# def handler500(request,*args,**argv):
#     response=render_to_response('500.html',{},context_instance=RequestContext(request))
#     response.status_code = 500
#     return response