from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login_page'),
    path('actions/do_login', views.login, name='login_action'),
    path('register', views.register_page, name='register_page'),
    path('actions/do_register', views.register, name='register_action')
]
