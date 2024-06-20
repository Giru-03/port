from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def sendmail(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = f'Name : {request.POST["fname"]} \t {request.POST["lname"]} \nEmail : {request.POST["email"]} \nMessage : \n\n{request.POST["message"]}'

        send_mail(
            subject,
            message,
            "takemynumber933withakissfree@gmail.com",
            ["sahil.murhekar2004@gmail.com"],
            fail_silently=False,
        )
        messages.success(request, "Mail Sent Successfully")
        return render(request, 'index.html')

    else:
        messages.success(request, "Mail Not Sent")
        return render(request, 'index.html')