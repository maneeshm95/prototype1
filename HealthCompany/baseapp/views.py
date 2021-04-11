from django.shortcuts import render
from django.http import HttpResponse
from hospital.models import Hospital
from patient.models import Patient
from .forms import ContactForm,ContactModelForm

def index(request):
    return render(request, 'index.html')

def all_model_queries(request):
    patients_age_greaterthan35 = Patient.objects.filter(age__gt=35)
    age35query = patients_age_greaterthan35.query

    patient_fname_lastname = Patient.objects.filter(
        first_name__startswith='J') | Patient.objects.filter(last_name__startswith='D')

    search_fname_lname_query = patient_fname_lastname.query

    context = {
        'patients_age_greaterthan35_key': patients_age_greaterthan35,
        'age35query_key': age35query,
        'patient_fname_lastname_key': patient_fname_lastname,
        'search_fname_lname_query_key': search_fname_lname_query
    }

    return render(request, 'modelQueries.html', context)


def contactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Your data is submitted")

    else:
        form = ContactForm()

    context = {
        'form_key': form
    }

    return render(request,'contact.html', context)

def ContactModelFormView(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Data is Submitted")
    else:
        form = ContactModelForm()

    context = {
        'form_key': form
    }

    return render(request,'contactus.html', context)
