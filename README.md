# 🎵 Music Academy Management System

A comprehensive web application designed for managing a **music academy**, built with **Django 5** and **Python 3.11**.  
This system enables administrators to manage teacher and student registrations, attendance tracking, tuition payments, and monthly financial reports — all in one place.

---

## ✨ Features

- 👩‍🏫 **Teacher & Student Management**  
  Admin can add, edit, and delete teacher and student records.

- 🕒 **Quick Attendance Registration**  
  A dedicated section for fast and easy attendance tracking.

- 💰 **Tuition & Instructor Share Management**  
  Automatically calculates monthly tuition fees and instructor shares.

- 📊 **Monthly Excel Reports**  
  Generates detailed Excel reports of financial data and performance using **Pandas**.

- 📈 **Admin Dashboard**  
  Displays an overview of key academy data:
  - Number of active teachers  
  - Number of students  
  - Attendance and payment summaries  

- 🇮🇷 **Persian Interface & Jalali Calendar Support**  
  Fully localized interface and date system designed for Iranian users.

---

## 🛠️ Technologies & Tools

| Component | Tool |
|------------|------|
| Programming Language | Python 3.11 |
| Web Framework | Django 5 |
| Database | SQLite (default Django database) |
| Libraries | Pandas, datetime, openpyxl |
| IDE | Visual Studio Code |

---

## 🚀 How to Run (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/music-academy-management.git
   cd music-academy-management



2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies
pip install -r requirements.txt

4. Run database migrations
python manage.py migrate

5. Start the local development server
python manage.py runserver

6. Open your browser and go to:
http://127.0.0.1:


# Project Structure
music_academy/
├── manage.py
├── requirements.txt
├── static/
├── templates/
├── students/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── teachers/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── reports/
│   ├── utils.py  # Functions for generating Excel reports
│   └── views.py
└── dashboard/
    ├── views.py
    └── templates/

Notes:
* User registration is managed only by the admin — no public sign-up form is available.

* The project is designed to run locally on the academy’s internal system (no internet connection required).

* All pages, content, and dates are displayed in Persian (Farsi) using the Jalali calendar.

👨‍🎨 Developer:
Parmis Sattari
🎼 Python Developer & Multimedia Enthusiast
📍 Developed for a private music academy in Iran


