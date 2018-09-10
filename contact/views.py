from django.shortcuts import render

from .models import ContactRequest
# Create your views here.


def contact_form(request):
    if request.method == 'POST':
        contact_request = ContactRequest()
        contact_request.name = request.POST['name']
        contact_request.email = request.POST['email']
        contact_request.message = request.POST['message']
        contact_request.save()
        return render(request, 'contact/contact_form.html', {'confirm': 'Your message has been sent, and we will follow up soon!'})
    else:
        return render(request, 'contact/contact_form.html')
