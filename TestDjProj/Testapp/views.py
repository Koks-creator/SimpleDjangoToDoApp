from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import ToDoList, Item
from .forms import CreateNewList, RegisterForm


# Create your views here.
@login_required()
def show_list(response, index: int):
    ls = ToDoList.objects.get(id=index)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("newItem"):
                task_text = response.POST.get("new")
                task_date = response.POST.get("date")

                if task_text:
                    ls.item_set.create(text=task_text, completed=False, end_date=task_date)

        return render(response, "list.html", {"ls": ls})
    return render(response, "home.html", {})


def home(response):
    if response.user.is_authenticated:
        return redirect("/my_lists")
    return render(response, "home.html", {})


@login_required()
def create_list(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            list_name = form.cleaned_data["name"]
            todo_list = ToDoList(name=list_name)
            todo_list.save()

            response.user.todolist.add(todo_list)

            return HttpResponseRedirect(f"/list/{todo_list.id}")
    else:
        form = CreateNewList()
    return render(response, "create_list.html", {"form": form})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})


def user_lists(response):
    return render(response, "user_todo_lists.html", {})


@login_required()
def my_lists(response):
    return render(response, "mylists.html", {})


@login_required()
def delete_list(response, list_id: int):
    ls = ToDoList.objects.get(id=list_id)
    ls.delete()

    return render(response, "mylists.html", {})


@login_required()
def delete_item(response, list_id: int, item_id: int):
    try:
        item = ToDoList.objects.get(id=list_id).item_set.get(id=item_id)
        item.delete()
    except (ToDoList.DoesNotExist, Item.DoesNotExist):
        return HttpResponse("List or item not found", content_type='text/plain')

    return redirect(f"/list/{list_id}")


@login_required()
def change_item_status(response, list_id: int, item_id: int):
    try:
        item = ToDoList.objects.get(id=list_id).item_set.get(id=item_id)
        if not item.completed:
            item.completed = True
        else:
            item.completed = False
        item.save()
    except (ToDoList.DoesNotExist, Item.DoesNotExist):
        return HttpResponse("List or item not found", content_type='text/plain')

    return redirect(f"/list/{list_id}")
