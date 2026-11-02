# MediCare HMS — Healthcare Management System

A Django-based web application for hospitals/clinics to manage patients, doctors,
appointments, prescriptions, medical history, and billing, with role-based
dashboards for Admin, Doctor, Patient, and Receptionist users.

## Features implemented in this scaffold

- **Secure login system** — custom `User` model with `role` field
  (Admin / Doctor / Patient / Receptionist), signup + login/logout views.
- **Patient management** — add, edit, delete, search, view profile + medical history.
- **Doctor management** — add, edit, delete, search, department assignment.
- **Appointments** — book, edit, cancel; doctors/patients only see their own.
- **Prescriptions** — diagnosis + a dynamic list of medicines (formset) per prescription.
- **Billing** — itemized bill (consultation, medicines, other charges, discount),
  auto-computed total, payment status/method.
- **Admin dashboard** — live counts (patients, doctors, pending appointments,
  unpaid bills) and a recent-appointments table.
- **Role-based dashboards** for doctors (their appointments) and patients
  (their appointments + bills).
- Django's built-in **/admin/** site is also enabled for power-user data management.

## Project structure

```
hms_workspace/
├── manage.py
├── requirements.txt
├── seed_data.py            # optional sample data loader
├── hms_project/             # project settings, urls, wsgi/asgi
├── accounts/                 # custom User model, login/signup
├── patients/                 # Patient, MedicalHistory
├── doctors/                  # Doctor, Department
├── appointments/              # Appointment
├── prescriptions/              # Prescription, Medicine
├── billing/                   # Bill
├── dashboard/                  # role-based home dashboard
├── templates/                  # all HTML templates (Bootstrap 5)
└── static/css/style.css        # custom styling on top of Bootstrap
```

## Setup

1. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate        # venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

   By default the project runs on **SQLite** — no extra setup needed.

2. **(Optional) Switch to MySQL**, as specified in the original project requirements:

   - Install MySQL and create a database (e.g. `hms_db`).
   - Install the MySQL client: `pip install mysqlclient` (needs MySQL dev headers;
     on Windows the easiest path is `pip install mysqlclient` with a matching
     prebuilt wheel, or install via XAMPP's MySQL + `pip install pymysql` and add
     `import pymysql; pymysql.install_as_MySQLdb()` to `hms_project/__init__.py`).
   - Set environment variables before running the server:

     ```bash
     export USE_MYSQL=1
     export DB_NAME=hms_db
     export DB_USER=root
     export DB_PASSWORD=yourpassword
     export DB_HOST=localhost
     export DB_PORT=3306
     ```

3. **Run migrations and create an admin account**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

   When prompted, or afterwards in `/admin/`, set that user's **role** to `ADMIN`
   (the signup form's role choices don't include Admin on purpose — admins are
   created via `createsuperuser` or promoted in Django admin).

4. **(Optional) Load sample data** for demoing:

   ```bash
   python manage.py shell < seed_data.py
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` — you'll be redirected to login.
   Django admin is at `http://127.0.0.1:8000/admin/`.

## Roles & access

| Role         | Created via                          | Sees                                             |
|--------------|---------------------------------------|---------------------------------------------------|
| Admin        | `createsuperuser` + set role=ADMIN    | Full dashboard, all patients/doctors/bills        |
| Receptionist | Signup form                           | Same dashboard as Admin (booking/billing focus)   |
| Doctor       | Signup form (auto-creates Doctor row) | Their own appointments/prescriptions              |
| Patient      | Signup form (auto-creates Patient row)| Their own appointments/bills, can book appointments|

## Notes / next steps for a production build

- Add permission checks per view (currently any logged-in user can reach any
  CRUD URL — role checks exist in querysets but not yet as hard `403`s).
- Add PDF export for prescriptions/bills (e.g. via `xhtml2pdf` or `weasyprint`).
- Add appointment time-slot conflict validation.
- Replace `SECRET_KEY` and set `DEBUG=False` + proper `ALLOWED_HOSTS` for deployment.
- Add automated tests (`python manage.py test`).
