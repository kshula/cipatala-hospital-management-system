# views.py
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Patient, MedicalRecord, LabTest
from .forms import ReceptionistLoginForm, PatientForm
from django.shortcuts import get_object_or_404


def index(request):
    patients = Patient.objects.all()  # Replace with your query based on your models
    context = {
        'patients': patients,
    }
    return render(request, 'index.html', context)

def complaints(request):
    return render(request, 'complaints.html')

def staff_login(request):
    return render(request, 'staff_login.html')

@csrf_protect
def reception_login(request):
    if request.method == 'POST':
        form = ReceptionistLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the receptionist dashboard
                return redirect('reception_dashboard')
    
    form = ReceptionistLoginForm()
    return render(request, 'reception_login.html', {'form': form})

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def process_reset_password(request):
    return render(request, 'process_reset_password.html')

def reception_dashboard(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient = patient_form.save()
            # Redirect to the patient details page
            return redirect('patient_detail', patient_id=patient.id)
    else:
        patient_form = PatientForm()

    # Render the reception dashboard with the patient registration form
    return render(request, 'reception_dashboard.html', {'patient_form': patient_form})

def save_complaint(request):
    if request.method == 'POST':
        title = request.POST['title']
        complaint_type = request.POST['complaint_type']
        complaint_text = request.POST['complaint_text']

        # Create a new complaint object and save it to the database
        new_complaint = Complaint.objects.create(
            title=title,
            complaint_type=complaint_type,
            complaint_text=complaint_text,
        )

        # You can perform additional actions here if needed

    return redirect('index') # Redirect to the index page after submitting the complaint

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})

def register_patient(request):
    if request.method == 'POST':
        # Handle form submission and create a new patient
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        # Add more fields as needed
        new_patient = Patient.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            # Assign more fields here
        )
        return redirect('dashboard')  # Redirect to the dashboard after registration
    return render(request, 'register_patient.html')  # Create a template for patient registration

# Add similar views for reading, updating, and deleting patient records

def suggest_tests(request, medical_record_id):
    if request.method == 'POST':
        # Handle form submission and suggest tests for a medical record
        test_name = request.POST['test_name']
        result = request.POST['result']
        medical_record = MedicalRecord.objects.get(pk=medical_record_id)
        LabTest.objects.create(
            medical_record=medical_record,
            test_name=test_name,
            result=result,
        )
        return redirect('dashboard')  # Redirect to the dashboard after suggesting tests
    return render(request, 'suggest_tests.html')  # Create a template for suggesting tests
