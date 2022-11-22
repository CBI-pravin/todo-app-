from django.shortcuts import render
from .models import todo
# Create your views here.


def all_task(request):

    tasks = todo.objects.all().order_by()[::-1]

    context = {'tasks':tasks}
    return render(request,'all_task.html',context)



def add_task(request):
    if request.method == "POST":
        task = request.POST.get('task')
        obj = todo.objects.create(task=task)
        obj.save()
    context ={}
    return render(request,'add_task.html',context)



def delete_task(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    print(q)
    if q:
        obj = todo.objects.filter(id=q)
        obj.delete()
        tasks = todo.objects.all().order_by()[::-1]

    else:
        tasks = todo.objects.all().order_by()[::-1]

    context = {'tasks':tasks}
    
    return render(request,'delete_task.html',context)


def mark_task(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    
    if q:
        obj = todo.objects.filter(id=q).update(status=True)
        

        
        tasks = todo.objects.filter(status = False).order_by()[::-1]

    else:
        tasks = todo.objects.filter(status = False).order_by()[::-1]

    context = {'tasks':tasks}
    
    return render(request,'mark_task.html',context)



def complete_task(request):
    tasks = todo.objects.filter(status = True).order_by()[::-1]

    context = {'tasks':tasks}
    return render(request,'complete_task.html',context)

    