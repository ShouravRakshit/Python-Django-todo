from django.shortcuts import render, redirect
from .models import Todo, Todoform
from django.http import HttpResponse

def HomePage(request):
    # getting all the objects
    todo_data = Todo.objects.all()
    # print(todo_data)
    content = {
        "todo": todo_data,
        "form": Todoform,
    }
    if request.method == "POST":
        data = request.POST
        form = Todoform(data)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    return render(request, "todoapps/index.html", {"data": content})


def Edittodo(request, id):
    try:
        list_data = Todo.objects.get(id=id)
        list_data.delete()
        return redirect("/")
    except:
        return redirect("/")
    
def Updatetodo(request, id):
    try:
        list_data = Todo.objects.get(id=id)

        return render(request, "todoapps/update.html", {"data": list_data})
    except:
        return redirect("/")
        

def Update(request):
    if request.method ==  'POST':
        data = request.POST
        update_data = data["item"]
        print(update_data)
        return redirect("/")
    else:
        return HttpResponse("<h1> Error </h1>")
