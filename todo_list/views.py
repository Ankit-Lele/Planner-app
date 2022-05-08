from django.shortcuts import render, redirect
from .models import List
from .models import Tom
from .models import Lists
from .models import List1
from .forms import Listform
from .forms import Listform1
from .forms import Listform2
from .forms import Listform3
from django.contrib import messages
from django.http import HttpResponse
#Home-page
def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)
          
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,('Item has been added to the List'))
            return render(request, "home.html",{'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, "home.html",{'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request , ('Item Has been Deleted!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id) 
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id) 
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item=List.objects.get(pk=list_id)

        form = Listform(request.POST or None, instance=item)    

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been edited!'))
            return redirect('home')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

def deleteAll(request):
    List.objects.all().delete()
    return redirect('home')

def deleteComplete(request):
    List.objects.filter(completed__exact=True).delete()
    return redirect('home')

def high(request, list_id):
    item = List.objects.get(pk=list_id)
    item.priority = True
    item.save()
    return redirect('home')


def prio(request):
         List.objects.filter(priority__exact=False).delete()
         return redirect('home')

def medium(request, list_id):
    item = List.objects.get(pk=list_id)
    item.priority = False
    item.save()
    return redirect('home')
#Sub-Task
def sub(request, lists_id):  
    if request.method == 'POST':
        form = Listform1(request.POST or None)
          
        if form.is_valid():
                form.save()
                all_tasks = Lists.objects.all()
                messages.success(request,('Task has been added to the List'))
                return render(request, "sub.html",{'all_tasks': all_tasks})
    else:
        all_tasks = Lists.objects.all()
        return render(request, "sub.html",{'all_tasks': all_tasks})



def cross(request, lists_id):
    task = Lists.objects.get(pk=lists_id) 
    task.done = True
    task.save()
    return redirect('home')


def ncross(request, lists_id):
    task = Lists.objects.get(pk=lists_id) 
    task.done = False
    task.save()
    return redirect('home')


def trash(request, lists_id):
    task = Lists.objects.get(pk=lists_id) 
    task.delete()
    messages.success(request , ('Task Has been Deleted!'))
    return redirect('sub.html')


def deleteAl(request):
    Lists.objects.all().delete()
    return redirect('home')

def deleteCompleted(request):
    Lists.objects.filter(done__exact=True).delete()
    return redirect('home')

def edits(request, lists_id):
    if request.method == 'POST':
        task=Lists.objects.get(pk=lists_id)

        form = Listform1(request.POST or None, instance=task)    

        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited!'))
            return redirect('home')
    
    else:
        task = Lists.objects.get(pk=lists_id)
        return render(request, 'edits.html', {'task': task})


#Tommorow's List
def tom(request, listss_id):  
    if request.method == 'POST':
        form = Listform2(request.POST or None)
          
        if form.is_valid():
                form.save()
                all_works = Tom.objects.all()
                messages.success(request,('Task has been added to the List'))
                return render(request, "tom.html",{'all_works': all_works})
    else:
        all_works = Tom.objects.all()
        return render(request, "tom.html",{'all_works': all_works})

def cut(request, listss_id):
    work = Tom.objects.get(pk=listss_id) 
    work.exec = True
    work.save()
    messages.success(request , ('Item Has been completed from tommorows list !'))
    return redirect('tom.html')

def dell(request, listss_id):
    work = Tom.objects.get(pk=listss_id) 
    work.exec = False
    work.save()
    return redirect('tom.html')


def dl(request, listss_id):
    work = Tom.objects.get(pk=listss_id) 
    work.delete()
    messages.success(request , ('Task Has been Deleted from tommorows list!'))
    return redirect('home')

def top(request, listss_id):
    work = Tom.objects.get(pk=listss_id)
    work.classify = True
    work.save()
    return redirect('home')

def low(request, listss_id):
    work = Tom.objects.get(pk=listss_id)
    work.classify = False
    work.save()
    return redirect('home')


def clas(request):
         Tom.objects.filter(classify__exact=False).delete()
         messages.success(request , (' All Low priority Tasks are Deleted from tommorows list!'))
         return redirect('tom.html')

def deleteeve(request):
    Tom.objects.all().delete()
    messages.success(request , (' All Tasks are Deleted from tommorows list!'))    
    return redirect('home')

def deleteComp(request):
    Tom.objects.filter(exec__exact=True).delete()
    return redirect('tom.html')


def change(request, listss_id):
    if request.method == 'POST':
        work = Tom.objects.get(pk=listss_id)

        form = Listform2(request.POST or None, instance=work)    

        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited in tommorows list!'))
            return redirect('home')
    
    else:
        work = Tom.objects.get(pk=listss_id)
        return render(request, 'change.html', {'work': work})


#Tommorow's Sub-List
def subs(request, list1_id):  
    if request.method == 'POST':
        form = Listform3(request.POST or None)
          
        if form.is_valid():
                form.save()
                all_things = List1.objects.all()
                messages.success(request,('Task has been added to the List'))
                return render(request, "subs.html",{'all_things': all_things})
    else:
        all_things = List1.objects.all()
        return render(request, "subs.html",{'all_things': all_things})

def quit(request, list1_id):
    thing = List1.objects.get(pk=list1_id) 
    thing.allright = True
    thing.save()
    return redirect('home')


def unquit(request, list1_id):
    thing = List1.objects.get(pk=list1_id) 
    thing.allright = True
    thing.save()
    return redirect('home')


def dust(request, list1_id):
    thing = List1.objects.get(pk=list1_id) 
    thing.delete()
    messages.success(request , ('Task Has been Deleted!'))
    return redirect('subs.html')


def deleteAd(request):
    List1.objects.all().delete()
    return redirect('home')

def deleteDone(request):
    List1.objects.filter(allright__exact=True).delete()
    return redirect('home')

def edits(request, lists_id):
    if request.method == 'POST':
        task=Lists.objects.get(pk=lists_id)

        form = Listform1(request.POST or None, instance=task)    

        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited!'))
            return redirect('home')
    
    else:
        task = Lists.objects.get(pk=lists_id)
        return render(request, 'edits.html', {'task': task})


def correct(request, list1_id):
    if request.method == 'POST':
        thing = List1.objects.get(pk=list1_id)

        form = Listform3(request.POST or None, instance=thing)    

        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited in tommorows list!'))
            return redirect('correct.html')
    
    else:
        thing = List1.objects.get(pk=list1_id)
        return render(request, 'correct.html', {'thing': thing})
