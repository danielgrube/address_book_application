from django.contrib.auth import login, authenticate
from django.shortcuts import render

from address_book_application.core.forms import CreateContactForm

def create_user(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.street_address = form.cleaned_data.get('street_address')
            user.save()
            password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=password)
            return redirect('home')
    else:
        form = CreateContactForm()
    return render(request,'create_contact.html', {'form': form})

def get_contact_profile(request, username):
    user = User.objects.get(username = username)
    return render(request, 'address_book_application/user_profile.html', {"user": user})