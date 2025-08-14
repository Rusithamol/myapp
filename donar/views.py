from django.shortcuts import render, redirect
from .forms import*
from .models import*
from django.contrib import messages

def patient_registration_page(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!")
            return redirect('patient')  
    else:
        form = PatientRegistrationForm()

    return render(request, 'patient.html', {'form': form})


def donar_registration_page(request):
    if request.method == "POST":
        form = DonarRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!")
            return redirect('donor')  

    else:
        form = DonarRegistrationForm()

    return render(request, 'donar.html', {'form': form})


def patienttable(request):
    context = {
        "all_patients": PatientRegistration.objects.all()  # Correct model query
    }
    return render(request, 'patienttable.html', context)
def donartable(request):
    context = {
        "all_patients": DonarRegistration.objects.all()  # Correct model query
    }
    return render(request, 'donartable.html', context)