from django.urls import path
from .views import admin_student_list, student_student_list, register, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/students/', admin_student_list, name='admin_student_list'),
    path('students/', student_student_list, name='student_student_list'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
