from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/model/form/add/', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),
    path('pretty/list/', views.pretty_list),
    path('pretty/add/', views.pretty_add),

    path('admin/list/', views.admin_list),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/<int:nid>/delete/', views.admin_delete),
    #path('admin/<int:nid>/reset/', views.admin_reset),
    path('logout/', views.logout),

    # 登录
    path('login/', views.login),
]