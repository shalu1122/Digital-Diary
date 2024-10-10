
from django.shortcuts import render, redirect
from .models import Contact, Contact
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import logout
from .models import User
from django.contrib.auth import authenticate
# def signup(request):
#     if request.method == 'POST':
#         # Handle signup form submission
#         email = request.POST['email']
#         password = request.POST['password']
#         name = request.POST['name']
#         messages.success(request, 'Signup successful!')
#         # Create a new user if desired

#     return render(request, 'signup.html')



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(name=name, email=email, password=password)
        messages.success(request, 'Signup successful. Please log in.')
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(f"username of user : {email}, password : {password}")
        user = User.objects.filter(email=email, password=password).first()
        if not user:
            messages.error(request, 'User not found.')
            return redirect('login')
        context={}
        context['username'] = user.name
        return redirect('all_contacts')
    return render(request, 'login.html')


# def add_contact(request):
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('all_contacts')

#     context = {'form': form}
#     return render(request, 'add_contact.html', context)


def add_contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        mobile = request.POST['mobile']
        name = request.POST['name']
        address = request.POST['address']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        dob = request.POST['dob']
        qualification = request.POST['qualification']
        nationality = request.POST['nationality']
        other_field = request.POST['other_field']

        contact = Contact(email=email, mobile=mobile, name=name, address=address, father_name=father_name,
                          mother_name=mother_name, dob=dob, qualification=qualification, nationality=nationality,
                          other_field=other_field)
        contact.save()
        messages.success(request, 'Contact added successfully.')
        return redirect('all_contacts')

    return render(request, 'add_contact.html')



# def edit_contact(request, contact_id):
#     contact_obj = Contact.objects.filter(id=contact_id).first()

#     context = {'contact_obj': contact_obj}
#     return render(request, 'edit_contact.html', context)

def edit_contact(request, contact_id):
    contact_obj = Contact.objects.filter(id=contact_id).first()
    if not contact_obj:
        messages.error(request, 'Unable to edit contact')
        return redirect('all_contacts')


    if request.method == 'POST':
        contact_obj.email = request.POST['email']
        contact_obj.mobile = request.POST['mobile']
        contact_obj.name = request.POST['name']
        contact_obj.address = request.POST['address']
        contact_obj.father_name = request.POST['father_name']
        contact_obj.mother_name = request.POST['mother_name']
        contact_obj.dob = request.POST['dob']
        contact_obj.qualification = request.POST['qualification']
        contact_obj.nationality = request.POST['nationality']
        contact_obj.other_field = request.POST['other_field']
        contact_obj.save()

        return redirect('all_contacts')
    messages.success(request, 'Contact edited successfully.')
    context = {'contact_obj': contact_obj}
    return render(request, 'edit_contact.html', context)



def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if not contact:
        messages.error(request, "Unable to delete contact")
        return redirect('all_contacts')
    contact.delete()
    messages.success(request, "Contact deleted successfully")
    return redirect('all_contacts')


def all_contacts(request):
    contacts = Contact.objects.all()
    print(f"all_contacts : {all_contacts}")
    context = {'contacts': contacts}
    return render(request, 'all_contacts.html', context)


