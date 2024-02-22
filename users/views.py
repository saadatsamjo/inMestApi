from django.shortcuts import redirect, render
from users.models import IMUser

def signUp(req):
    username = req.POST['username']
    first_name = req.POST['first_name']
    last_name = req.POST['first_name']
    phone_number = req.POST['phone_number']
    password = req.POST['password']

    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number
    )

    new_user.set_password(password)
    new_user.save()
    return render('success_page')
