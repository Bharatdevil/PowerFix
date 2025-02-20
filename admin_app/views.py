from django.shortcuts import render ,redirect,get_object_or_404
from admin_app.models import Admin
from profile.models import Customer,Electrician
from service_app.models import Service
from book_app.models import Booking

# Create your views here.
def admin_dashboard(request):
    # if 'admin_username' in request.session:
    #     return render(request, 'admin_dashboard.html')
    # else:   
    #     return redirect('admin_app:admin_login')
    return render(request,'admin_dashboard.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            admin = Admin.objects.get(a_login_id=username)
            if admin.a_password==password:
                request.session['admin_id']=admin.a_id
                request.session['admin_username']=username
                print(request.session.get("admin_username"))
                return redirect('admin_app:admin_dashboard')
            else:
                print("else")
                return render(request,'login.html',{'error': 'Invalid username or password.'})
                
        except Admin.DoesNotExist:
            print("exe")
            return render(request,'login.html',{'error': 'Invalid username or password.'})
    
    message = request.session.pop('status',None)
    return render(request,'login.html',{'message':message})

def admin_logout(request):
    request.session.flush()
    request.session['status'] = "You have been logged out."
    return redirect('admin_app:admin_login')


def view_users(request):
    if request.method == "GET":
        customers = Customer.objects.values("c_id", "c_fullname", "c_login_id", "c_email", "c_address", "c_contact")  
        print(customers)      
        return render(request, "view_users.html", {"customers": customers} )
    
def update_user(request,c_id):
    customer = get_object_or_404(Customer, c_id=c_id)
    print(customer.c_id)

    if request.method == "POST":
        customer.c_fullname = request.POST.get('c_fullname')
        customer.c_email = request.POST.get('c_email')
        customer.c_address = request.POST.get('c_address')
        customer.c_contact = request.POST.get('c_contact')

        customer.save()

        request.session['customer_update'] = "User updated successfully"
        
        return redirect('admin_app:view_users')

    return render(request,'user_update_admin.html',{'customer':customer})
    

def delete_user(request,c_id):
    customer = get_object_or_404(Customer, c_id=c_id)
    customer.delete()
    print("inside del")
    return redirect('admin_app:view_users')


def create_service(request):
    if request.method == "POST":
        s_name = request.POST.get('s_name')
        s_description = request.POST.get('s_description')
        s_price = request.POST.get('s_price')
        electrician_id = request.POST.get('e_id')

        # Retrieve Electrician instance using ID
        electrician = Electrician.objects.get(e_id=electrician_id)

        # Create and save the Service instance
        Service.objects.create(
            s_name=s_name,
            s_description=s_description,
            s_price=s_price,
            e_id=electrician
        )

        return redirect('admin_app:view_service')  # Redirect after successful creation

    # Fetch all electricians for the dropdown
    electricians = Electrician.objects.all()
    return render(request, 'create_service.html', {'electricians': electricians})


def view_service(request):
    if request.method == "GET":
        services = Service.objects.all()
        print('hello world',services)
        return render(request,'view_services.html',{"services":services})
    
def delete_service(request,s_id):
    service = get_object_or_404(Service, s_id=s_id)
    service.delete()
    return redirect('admin_app:view_service')

# def update_service(request,s_id,e_id):
#     service = get_object_or_404(Service, s_id=s_id)
#     electricians = get_object_or_404(Electrician, e_id=e_id)
#     # electricians = Electrician.objects.all()
#     print(electricians)
#     print(service.s_id)
    
#     if request.method == "POST":
#         service.s_name = request.POST.get('s_name')
#         service.s_description = request.POST.get('s_description')
#         service.s_price = request.POST.get('s_price')

#         e_id_value = request.POST.get('e_id')  # This should be a valid primary key for Electrician
#         print("inside if",e_id_value)
#         if e_id_value:
#             service.e_id = get_object_or_404(Electrician, e_id=e_id_value)
#         service.save()    
#         # request.session['service_update'] = "Service updated successfully"
    
#         return redirect('admin_app:view_service')

#     return render(request,'update_service.html',{'service':service ,'electricians': electricians})


def update_service(request, s_id):
    service = get_object_or_404(Service, s_id=s_id)
    electricians = Electrician.objects.all()

    if request.method == 'POST':
        # Get data from form
        service.s_name = request.POST['s_name']
        service.s_description = request.POST['s_description']
        service.s_price = request.POST['s_price']
        service.e_id = Electrician.objects.get(e_id=request.POST['e_id'])  # Update the Electrician using e_id
        
        # Save the updated service
        service.save()
        return redirect('admin_app:view_service')  # Redirect to the list of services or wherever you want

    context = {
        'service': service,
        'electricians': electricians,
    }

    return render(request, 'update_service.html', context)



#electrician 
def view_electrician(request):
    if request.method == "GET":
        electricians = Electrician.objects.values("e_id", "e_fullname", "e_login_id", "e_email", "e_address", "e_contact","e_qualification")  
        print(electricians)      
        return render(request, "view_electrician.html", {"electricians": electricians} )
    
def update_electrician(request,e_id):
    electrician = get_object_or_404(Electrician, e_id=e_id)
    print(electrician.e_id)

    if request.method == "POST":
        electrician.e_fullname = request.POST.get('e_fullname')
        electrician.e_email = request.POST.get('e_email')
        electrician.e_address = request.POST.get('e_address')
        electrician.e_contact = request.POST.get('e_contact')
        electrician.e_qualification = request.POST.get('e_qualification')

        electrician.save()

        request.session['electrician_update'] = "User updated successfully"
        
        return redirect('admin_app:view_electrician')

    return render(request,'electrician_update_admin.html',{'electrician':electrician})
    

def delete_electrician(request,e_id):
    electrician = get_object_or_404(Electrician, e_id=e_id)
    electrician.delete()
    print("inside del")
    return redirect('admin_app:view_users')


def admin_view_bookings(request):
    # Fetch all booking records with related Customer, Service, and Electrician details
    bookings = Booking.objects.select_related('c_id', 's_id__e_id')

    return render(request, 'admin_view_bookings.html', {'bookings': bookings})
