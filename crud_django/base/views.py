
from multiprocessing import context
from turtle import title
from urllib import response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
# Create your views here.

 
class TaskList(LoginRequiredMixin,ListView):
    '''Show home page'''
    model=Task
    #to change the default variable 
    context_object_name= 'tasks'
    def get_queryset(self):
        '''show value by input, or give all items with complete false and correspond to user '''
        search_input=self.request.GET.get('search_area')
        if search_input:

            objects=Task.objects.filter(complete=False,user=self.request.user,title__icontains=search_input)
            return objects
        else:
            objects=Task.objects.filter(complete=False,user=self.request.user)
            return objects
    

    
class TaskHistory(LoginRequiredMixin,ListView):
    model=Task
    context_object_name= 'history'
    template_name='base/history.html'
    def get_queryset(self):
        '''this function show all items which have been completed'''
        search_input=self.request.GET.get('search_area')
        if search_input:

            objects=Task.objects.filter(complete=False,user=self.request.user,title__icontains=search_input)
            return objects
        else:
            objects=Task.objects.filter(complete=False,user=self.request.user)
            return objects
        
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model= Task
    context_object_name='task'
    #to modify default template name
    template_name='base/task.html'
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description',]
    success_url= reverse_lazy('application:taskList')    
    template_name='base/create.html'
    def form_valid(self,form):
        form.instance.user=self.request.user
        #TaskCreate the same as the name class
        return super(TaskCreate,self).form_valid(form)
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    template_name='base/task_update.html'
    success_url= reverse_lazy('application:taskList')  
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task    
    template_name='base/task_delete.html'
    success_url= reverse_lazy('application:history')  

class TaskLogin(LoginView):
    '''Create a new user'''
    template_name: str='base/login.html'
    fields='__all__'
    redirect_authenticated_user: bool=True
    def get_success_url(self) -> str:

        return reverse_lazy('application:taskList')
class TaskRegister(FormView):
    '''create a new user'''
    template_name: str="base/register.html" 
    form_class=UserCreationForm 
    redirect_authenticated_user=True
    success_url= reverse_lazy('application:taskList')
    def form_valid(self,form):
        '''valid the informacion and save it'''
        user=form.save()
        if user is not None:
            login(self.request,user)

        return super(TaskRegister,self).form_valid(form) 
    def get(self,*args, **kwargs):
        '''if the user is already log in go to tasklist, another hand go to TaskRegister page'''
        if self.request.user.is_authenticated:
            return redirect('application:taskList')
        return super(TaskRegister,self).get(*args, **kwargs)


# def handler404(request,*args,**argv):
#     response=render_to_response('404.html',{},context_instance=RequestContext(request))
#     response.status_code=404
#     return response

# def handler500(request,*args,**argv):
#     response=render_to_response('500.html',{},context_instance=RequestContext(request))
#     response.status_code = 500
#     return response