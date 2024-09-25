from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

# Create your views here.
def index(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()

    filter_option = request.GET.get('filter', 'all')
    if filter_option == 'active':
        item_list = Todo.objects.filter(completed=False).order_by("-date")
    elif filter_option == 'completed':
        item_list = Todo.objects.filter(completed=True).order_by("-date")
    else:
        item_list = Todo.objects.order_by("-date")

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
        "filter_option": filter_option,
    }
    return render(request, 'index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Todo Item removed!!")
    return redirect('todo')

def complete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Todo, id=item_id)
        item.completed = True
        item.save()
        messages.info(request, "Todo Item completed!!")
        return redirect('todo')  
    else:
        return redirect('todo') 