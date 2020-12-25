"""testa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page,name="login"),
    path("login_validate",views.login_validate,name="login"),
    path("home",views.home,name="home"),
    path("logout",views.logout,name="logout"),
    path("create_customer",views.create_customer,name="create"),
    path("upload_customer_data",views.upload_customer_data,name="upload_data"),
    path("edit_customer",views.edit_customer,name="edit"),
    path("edit_customer_data",views.edit_customer_data,name="edit_submit"),
    path("delete_customer",views.delete_customer,name="delete"),
    path("delete_customer_data",views.delete_customer_data,name="delete_data"),
    path("view_customer",views.view_customer,name="view"),
    path("search_customer",views.search_customer,name="search")
]
