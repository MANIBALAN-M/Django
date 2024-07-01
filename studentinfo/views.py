from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm  

students = [
    {'name': 'mani', 'age': 20, 'grade': 'A', 'address': '123 Main St', 'phone': '555-555-5555'},
    {'name': 'balan', 'age': 22, 'grade': 'B', 'address': '456 Elm St', 'phone': '555-555-5556'},
    {'name': 'kutty', 'age': 21, 'grade': 'A', 'address': '789 Oak St', 'phone': '555-555-5557'},
]

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_student_list(request):
    return render(request, 'admin_student_list.html', {'students': students})

@login_required
def student_student_list(request):
    limited_students = [{'name': student['name'], 'age': student['age'], 'grade': student['grade']} for student in students]
    return render(request, 'student_student_list.html', {'students': limited_students})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student_student_list')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_student_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


