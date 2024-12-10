from django.shortcuts import render, redirect
from .models import Todo  # Import the Todo model

# View for displaying the list of todos
def todo_list(request):
    todos = Todo.objects.order_by('-id')  # Get all the Todo items
    return render(request, 'todo/index.html', {'todos': todos})

# View for creating a new todo
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Ensure the model name is correctly referenced
        Todo.objects.create(title=title, description=description)
        
        return redirect('todo_list')  # Redirect to the homepage after creating a todo
    # return render(request, 'todo/create.html')  # Render a form page for creating a new todo (optional)


def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.delete()
    return redirect('todo_list')
