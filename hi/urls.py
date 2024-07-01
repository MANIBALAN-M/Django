from django.urls import path
from . import views

app_name = "hi"

urlpatterns = [
    path("", views.index , name="index"),
    path("post/<str:post_id>",views.detail, name="detail"),
    path("google.com/",views.new_url , name ='new_url'),
    path("old_url/",views.old_url , name ='old_url')
]