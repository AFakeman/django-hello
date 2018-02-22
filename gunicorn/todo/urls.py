from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('actions/add_todo', views.add_todo, name='add_todo_action'),
    path('actions/apply_todo_changes', views.apply_todo_changes, name='apply_todo_changes_action'),
    path('actions/do_login', views.login, name='login_action'),
    path('actions/do_register', views.register, name='register_action'),
    path('actions/do_log_out', views.log_out, name='log_out_action'),
    path('list', views.todo_view, name='todo_view'),
    path('login', views.login_page, name='login_page'),
    path('register', views.register_page, name='register_page'),
]
