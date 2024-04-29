from django.contrib import admin
from django.urls import path
from hms_app.views import register_patient, suggest_tests, index, save_complaint, complaints, staff_login, staff_dashboard, forgot_password, reset_password, process_reset_password, reception_dashboard, reception_login, patient_detail

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('complaints/', complaints, name='complaint_page'),
    path('staff-login/', staff_login, name='staff_login'),
    path('reception-login/', reception_login, name='reception_login'),
    path('staff-dashboard/', staff_dashboard, name='staff_dashboard'),
    path('save-complaint/', save_complaint, name='save_complaint'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/', reset_password, name='reset_password'),
    path('reception-dashboard/', reception_dashboard, name='reception_dashboard'),
    path('process-password/', process_reset_password, name='process_reset_password'),
    path('register/', register_patient, name='register_patient'),
    path('patient/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('suggest-tests/<int:medical_record_id>/', suggest_tests, name='suggest_tests'),

    # Add more URLs for other views
]
