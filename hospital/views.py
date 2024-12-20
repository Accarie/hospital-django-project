from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient, Appointment, Schedule
from .forms import DoctorForm, PatientForm, AppointmentForm, ScheduleForm
from django.contrib.auth.decorators import login_required

# Index Page
@login_required(login_url='login') 
def index(request):
    return render(request, 'index.html')

# Doctors Views
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors':doctors})
def doctor_create(request):    
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctor_create.html', {'form': form})

def doctor_edit(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_edit.html', {'form': form})

def doctor_delete(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    return render(request, 'doctor_delete.html', {'doctor': doctor})

# Patients Views
def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})
def patient_create(request):    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'patient_create.html', {'form': form})

def patient_edit(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_edit.html', {'form': form})

def patient_delete(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
    return render(request, 'patient_delete.html', {'patient': patient})

# Appointments Views
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})
def appointment_create(request):    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_create.html', {'form': form})

def appointment_edit(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_edit.html', {'form': form})

def appointment_delete(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments')
    return render(request, 'appointment_delete.html', {'appointment': appointment})

# Schedules Views
def schedules(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedules.html', {'schedules':schedules})
def schedule_create(request):    
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedules')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_create.html', {'schedules': schedules, 'form': form})

def schedule_edit(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedules')  # Redirect to the schedule list page
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedule_edit.html', {'form': form})


def schedule_delete(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedules')
    return render(request, 'schedule_delete.html', {'schedule': schedule})
