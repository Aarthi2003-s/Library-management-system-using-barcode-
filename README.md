📚 Library Management System (LMS)
A web-based application built using Django and MySQL that streamlines library operations through barcode-based book borrowing and returning. Designed for students and administrators to simplify the management of books, users, and library transactions.

🔧 Features
✅ Admin Module
Add/Edit/Delete Users

Generate Barcode for User Registration Number

Add/Edit/Delete Books

Generate Barcode for Book Access Number

View Reports (Total Users, Books, Borrowed, Returned)

✅ Student/User Module
Borrow Books via Barcode Scanning

Return Books via Barcode Scanning

✅ Book Search Module
Search Books by Title, Author, or Access Number

View Real-Time Book Availability

💻 Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript, Bootstrap
Backend	Python (Django Framework)
Database	MySQL
Barcode Generator	python-barcode

🛠 Installation
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
2. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Configure MySQL database in settings.py:
python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lib_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
4. Run migrations:
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Start the development server:
bash
Copy
Edit
python manage.py runserver
🖼 Sample Screens
Admin Dashboard

User Registration & Management

Book CRUD with Barcode

Scan Book/User Interface

Real-time Due Alerts

Reports

📌 Future Enhancements
Email Notifications for Due Dates

Mobile App Integration

Fine Payment Gateway

Role-based Access Control (Admin, Staff)

🙏 Acknowledgment
Project submitted as part of M.Sc Computer Science at The Madura College, Madurai under the guidance of Prof. K. Rajasaravanakumar.

📝 License
This project is for academic use only.

