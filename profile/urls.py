from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  # Login or Register page
    path('role_redirect/', views.role_redirect, name='role_redirect'),  # Handles redirection
    path('about_us/', views.about_us, name='about_us'),

    #customer pages
    path('customer/login/check/', views.customer_login_check, name='customer_login_check'),
    path('customer/register/check', views.customer_register_check, name='customer_register_check'),
    path('customer/register/', views.customer_register, name='customer_register'),
    path('customer/login/', views.customer_login, name='customer_login'),
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    path('customer/update/',views.update_customer,name="update_customer"),
    path('customer/logout/', views.customer_logout, name='customer_logout'),


    #electrician pages
    path('electrician/login', views.electrician_login, name='electrician_login'),
    path('electrician/register/', views.electrician_register, name='electrician_register'),
    path('electrician/login/check/', views.electrician_login_check, name='electrician_login_check'),
    path('electrician/register/check', views.electrician_register_check, name='electrician_register_check'),
    path('electrician/profile/', views.electrician_profile, name='electrician_profile'),
    path('electrician/update/',views.update_electrician,name="update_electrician"),
    path('view_booking_electrician/',views.view_booking_electrician,name="view_booking_electrician"),
    path('electrician/logout/', views.electrician_logout, name='electrician_logout'),

    #service pages
    path('view_service/',views.view_service,name="view_service"),
    # path('view_service/',views.view_service,name="view_service"),



    #booking pages
    path('save_booking/<int:s_id>/',views.save_booking,name="save_booking"),
    path('view_booking/',views.view_booking,name="view_booking"),
    path('accept_booking/<int:b_id>/',views.accept_booking,name="accept_booking"),
    path('complete_booking/<int:b_id>/', views.complete_booking, name='complete_booking'),

]

