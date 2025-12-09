from django.shortcuts import render,redirect
from .models import Note, Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):

    if request.user.is_authenticated:

        # Basic stats
        notes_count = Note.objects.filter(user=request.user).count()
        tasks_total = Task.objects.filter(user=request.user).count()
        tasks_pending = Task.objects.filter(user=request.user, status="pending").count()
        tasks_done = Task.objects.filter(user=request.user, status="done").count()

        # Latest Notes (3 most recent)
        latest_notes = Note.objects.filter(user=request.user).order_by('-created_at')[:3]

        # Latest Tasks (3 most recent)
        latest_tasks = Task.objects.filter(user=request.user).order_by('-created_at')[:3]

        # Today's Tasks
        today = timezone.now().date()
        todays_tasks = Task.objects.filter(user=request.user, due_date=today)

        # Greeting
        current_hour = timezone.now().hour
        if current_hour < 12:
            greeting = "Good Morning"
        elif current_hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

    else:
        # Guest user fallback
        notes_count = tasks_total = tasks_pending = tasks_done = 0
        latest_notes = latest_tasks = todays_tasks = []
        greeting = "Welcome"

    context = {
        # Stats
        "notes_count": notes_count,
        "tasks_total": tasks_total,
        "tasks_pending": tasks_pending,
        "tasks_done": tasks_done,

        # Lists
        "latest_notes": latest_notes,
        "latest_tasks": latest_tasks,
        "todays_tasks": todays_tasks,

        # UI
        "greeting": greeting,
    }

    return render(request, "index.html", context)


@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        Note.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect("index")

    return render(request, "add_note.html")

@login_required
def view_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "view_notes.html", {"notes": notes})

@login_required
def add_task(request):
    if request.method == "POST":
        name = request.POST.get("name")
        due_date = request.POST.get("due_date")

        Task.objects.create(
            user=request.user,
            name=name,
            due_date=due_date,
            status="pending"
        )

        return redirect("index")

    return render(request, "add_task.html")

@login_required
def view_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "view_tasks.html", {"tasks": tasks})
