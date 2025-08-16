# Kelaasor

## User & Purchase Management Website
### A backend system built with **Django** and **Django REST Framework** for managing users, bootcamps, transactions, blogs, and support tickets.  The project is designed mainly for **site administrators**, with additional access levels for **technicians**.

---
## ✨ Features

### 👥 User Management
- Register, login, and authentication (JWT / Session-based)  
- Role-based access control (Admin, Technician, User)  
- Profile and permission management  

### 🎓 Bootcamps
- Create, update, and delete bootcamp entries  
- Assign users to bootcamps  
- Track progress and attendance  

### 💳 Transactions
- Record and manage financial transactions  
- Link transactions to users and bootcamps  
- Transaction history and reporting  

### 📝 Blogs
- Add, edit, and delete blog posts  
- Public and private visibility options  
- Category and tag management  

### 🎧 Support
- Support ticket creation and management  
- Assign tickets to technicians  
- Notifications via **Celery** (email/SMS)  

---

## 🛠 Tech Stack
- **Backend Framework:** Django + Django REST Framework  
- **Database:** PostgreSQL + PostGIS (geospatial support)  
- **Geo Support:** GeoDjango  
- **Task Queue:** Celery + Redis  
- **Email:** Google API  
- **SMS:** Kavenegar API  
- **Authentication:** JWT / Session-based  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   https://github.com/Mohamad-Moghadam/final_project.git
   cd final_project