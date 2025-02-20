from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# from .forms import CustomerRegistrationForm
from .models import Customer,Electrician
from service_app.models import Service
from book_app.models import Booking

#home view
def home(request):
    return render(request, 'profile/home.html')
#login view
def login_view(request):
    return render(request, 'profile/login.html')

def about_us(request):
    return render(request, 'profile/about_us.html' )


#customer pages
def customer_register(request):
    return render(request, 'profile/customer_register.html')

def customer_login(request):
    return render(request, 'profile/customer_login.html')

#electrician pages
def electrician_register(request):
    return render(request, 'profile/electrician_register.html')

def electrician_login(request):
    return render(request, 'profile/electrician_login.html')



def customer_profile(request):
    customer = Customer.objects.filter(c_id=request.session['customer_id']).first()
    if not customer:
    # Handle the case where no customer is found
        return redirect('customer_login') 
    
    customer_id = request.session['customer_id']

    # customer = Customer.objects.get()
    print(customer)
    # return render(request, 'profile/customer_profile.html')
    return render(request, 'profile/customer_profile.html')


#role view
def role_redirect(request):
    if request.method == 'POST':
        role = request.POST['role']
        action = request.POST['action']
        if role == 'customer' and action == 'login':
            return redirect('customer_login')
        elif role == 'customer' and action == 'register':
            return redirect('customer_register')
        elif role == 'electrician' and action == 'login':
            return redirect('electrician_login')
        elif role == 'electrician' and action == 'register':
            return redirect('electrician_register')
    


# Customer Registration check
def customer_register_check(request):
    if request.method == 'POST':
        c_fullname = request.POST['c_fullname']
        c_username = request.POST['c_username']
        c_password = request.POST['c_password']  
        c_email = request.POST['c_email']
        c_contact = request.POST['c_contact']
        c_address = request.POST['c_address']

        if Customer.objects.filter(c_login_id=c_username).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'profile/customer_register.html')
    
        Customer.objects.create(
            c_fullname=c_fullname,
            c_login_id=c_username,
            c_password=c_password,
            c_email=c_email,
            c_contact=c_contact,
            c_address=c_address
        )
        messages.success(request, "Registration successful! Please login.")
        print("saved customer details")
        return redirect('customer_login')
    return render(request, 'profile/customer_register.html')



# Customer Login check
def customer_login_check(request):
    if request.method == 'POST':
        login_id = request.POST['login_id']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(c_login_id=login_id, c_password=password)
            request.session['customer_id'] = customer.c_id
            request.session['customer_name'] = customer.c_fullname
            return render(request,'profile/customer_profile.html',{'customer':customer,'message':'Login successfully'})

        except Customer.DoesNotExist:
             return render(request,'profile/customer_login.html',{'error': 'Invalid username or password.'})            
    return render(request, 'profile/customer_login.html')

# Customer Logout 
def customer_logout(request):
    # delete session
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('home')




def update_customer(request):
    # Fetch the customer_id from session
    customer_id = request.session.get('customer_id')

    # If no customer_id in session, redirect to login page
    if not customer_id:
        return redirect('customer_login')  # Redirect to the login page

    # Fetch the customer object using the customer_id
    customer = get_object_or_404(Customer, c_id=customer_id)

    # If the form is submitted, update the customer details
    if request.method == 'POST':
        # Update the customer with the form data
        customer.c_fullname = request.POST.get('c_fullname')
        customer.c_email = request.POST.get('c_email')
        customer.c_contact = request.POST.get('c_contact')
        customer.c_address = request.POST.get('c_address')
        customer.save()  # Save the updated details to the database

        # Optionally, you can set a success message and redirect
        return redirect('customer_profile')  # Redirect to profile or wherever you want

    # Render the update form with customer details prefilled
    return render(request, 'profile/customer_update.html', {'customer': customer})





# Electrcian Registration check
def electrician_register_check(request):

    if request.method == 'POST':
        e_fullname = request.POST['e_fullname']
        e_username = request.POST['e_login_id']
        e_password = request.POST['e_password']  # Hash the password
        e_email = request.POST['e_email']
        e_contact = request.POST['e_contact']
        e_address = request.POST['e_address']
        e_qualification = request.POST['e_qualification']
        print("if post")

        if Electrician.objects.filter(e_login_id=e_username).exists():
            messages.error(request, "Username already taken!")
            print("if check")
            return render(request, 'profile/electrician_register.html')
            
        Electrician.objects.create(
            e_fullname=e_fullname,
            e_login_id=e_username,
            e_password=e_password,
            e_email=e_email,
            e_contact=e_contact,
            e_address=e_address,
            e_qualification=e_qualification
        )
        messages.success(request, "Registration successful! Please login.")
        print("saved customer details")
        return redirect('electrician_login')
    return render(request, 'profile/electrician_register.html')


def electrician_profile(request):
    return render(request,'profile/electrician_profile.html')

def update_electrician(request):
    # Fetch the electrician_id from session
    electrician_id = request.session.get('electrician_id')

    # If no customer_id in session, redirect to login page
    if not electrician_id:
        return redirect('electrician_login')  # Redirect to the login page

    # Fetch the customer object using the customer_id
    electrician = get_object_or_404(Electrician, e_id=electrician_id)

    # If the form is submitted, update the customer details
    if request.method == 'POST':
        # Update the customer with the form data
        electrician.e_fullname = request.POST.get('e_fullname')
        electrician.e_email = request.POST.get('e_email')
        electrician.e_contact = request.POST.get('e_contact')
        electrician.e_address = request.POST.get('e_address')
        electrician.e_qualification = request.POST.get('e_qualification')
        
        electrician.save()  # Save the updated details to the database

        # Optionally, you can set a success message and redirect
        return redirect('electrician_profile')  # Redirect to profile or wherever you want

    # Render the update form with customer details prefilled
    return render(request, 'profile/electrician_update.html', {'electrician': electrician})




def electrician_login_check(request):
    if request.method == 'POST':
        print("if")
        login_id = request.POST['login_id']
        password = request.POST['password']
        try:
            
            # Authenticate electrician with provided credentials
            electrician = Electrician.objects.get(e_login_id=login_id, e_password=password)
            print("try")

            # Set session variables
            request.session['electrician_id'] = electrician.e_id
            request.session['electrician_name'] = electrician.e_fullname

            # Redirect to profile page
            return redirect('electrician_profile')  # Use a URL name for redirection

        except Electrician.DoesNotExist:
            print("except")
            # Return error message if credentials are invalid
            return render(request, 'profile/electrician_login.html', {
                'error': 'Invalid username or password.'
            })

    # Default to rendering the login page on GET request
    return render(request, 'profile/electrician_login.html')



def view_booking_electrician(request):
    # Retrieve customer ID from session
    electrician_id = request.session.get('electrician_id')
    print(electrician_id)

    # Check if customer_id exists in session
    if electrician_id:
        # Fetch bookings related to the logged-in customer using select_related for optimized query
        # booking = Booking.objects.select_related('s_id', 'c_id')
        # print(booking)
        booking = Booking.objects.select_related('s_id', 'c_id').filter(s_id__e_id=electrician_id)
        print("Filtered Bookings:", booking)
        
        # Render the bookings in the template
        return render(request, 'profile/view_booking_electrician.html', {'booking': booking})
    
    # If no customer_id found in session, redirect or show an error page
    return render(request, 'service_booking_failed.html', {"error": "User not logged in!"})

# Electrician Logout 
def electrician_logout(request):
    # delete session
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('home')








#services
def view_service(request):
    if request.method == "GET":
        services = Service.objects.all()
        print('hello world',services)
        return render(request,'profile/view_service.html',{"services":services})






#booking
def book_service(request):
    if request.method == "GET":
        services = Service.objects.all()
        print('hello world',services)
        return render(request,'profile/view_service.html',{"services":services})
    

import datetime
def save_booking(request, s_id):
    
    service = Service.objects.get(s_id=s_id)
    service_id=service.s_id

    # Get customer_id
    customer_id = request.session.get('customer_id')

    # Check if the customer_id 
    if customer_id:
        # Check if the request method is POST
        print(customer_id)
        if request.method == "POST":
            current_datetime = datetime.datetime.now()
            # Create a new booking
            booking = Booking(
                b_status="Pending",  
                b_amt=service.s_price,  
                b_date=current_datetime,  # Use current date or selected date
                c_id_id=customer_id,  # Use customer_id from session
                s_id_id=service_id
            )
            booking.save()

            # Redirect the user to  profile page to view their bookings
            return redirect('view_booking')  

    # If customer_id doesn't exist in the session or any other issue
    return render(request, 'profile/view_service.html')  



     

def view_booking(request):
    # Retrieve customer ID from session
    customer_id = request.session.get('customer_id')

    # Check if customer_id exists in session
    if customer_id:
        # Fetch bookings related to the logged-in customer using select_related for optimized query
        booking = Booking.objects.select_related('s_id', 's_id__e_id').filter(c_id=customer_id)
        
        # Render the bookings in the template
        return render(request, 'profile/view_booking.html', {'booking': booking})
    
    # If no customer_id found in session, redirect or show an error page
    return render(request, 'view_service.html', {"error": "User not logged in!"})


def accept_booking(request, b_id):
    # Get the booking by its ID
    booking = get_object_or_404(Booking, b_id=b_id)
    
    # Update the status to 'Accepted'
    if booking.b_status == "Pending":
        booking.b_status = "Accepted"
        booking.save()
    
    # Redirect back to the electrician's booking list page
    return redirect('view_booking_electrician')

def complete_booking(request, b_id):
    # Get the booking by its ID
    booking = get_object_or_404(Booking, b_id=b_id)
    
    # Update the status to 'Completed'
    if booking.b_status == "Accepted":
        booking.b_status = "Completed"
        booking.save()
    
    # Redirect back to the electrician's booking list page
    return redirect('view_booking_electrician')