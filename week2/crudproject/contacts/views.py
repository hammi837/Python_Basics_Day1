from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact

def contacts(request):
    # CREATE
    if request.method == "POST" and 'create' in request.POST:
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return redirect('contacts')

    # UPDATE
    if request.method == "POST" and 'update' in request.POST:
        contact = get_object_or_404(Contact, id=request.POST['id'])
        for field in ['name', 'email', 'subject', 'message']:
            setattr(contact, field, request.POST[field])
        contact.save()
        return redirect('contacts')

    # DELETE
    if request.method == "POST" and 'delete' in request.POST:
        contact = get_object_or_404(Contact, id=request.POST['id'])
        contact.delete()
        return redirect('contacts')

    # READ
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

