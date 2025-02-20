from django.urls import path
from . import views 

app_name = 'admin_app'

urlpatterns = [
    path('',views.admin_login,name="admin_login"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'), 
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('admin/bookings/view/', views.admin_view_bookings, name='admin_view_bookings'),
    
    path('view_users/',views.view_users,name="view_users"),
    path('update_user/<int:c_id>/',views.update_user,name="update_user"),
    path('delete_user/<int:c_id>/',views.delete_user,name="delete_user"),

    path('create_service/',views.create_service,name="create_service"),
    path('view_service/',views.view_service,name="view_service"),
    path('delete_service/<int:s_id>/',views.delete_service,name="delete_service"),
    path('update_service/<int:s_id>/',views.update_service,name="update_service"),

    path('view_electrician/',views.view_electrician,name="view_electrician"),
    path('update_electrician/<int:e_id>/',views.update_electrician,name="update_electrician"),
    path('delete_electrician/<int:e_id>/',views.delete_electrician,name="delete_electrician"),
]