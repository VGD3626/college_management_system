# College Management System: Streamlining Operations & Communication


## Overview

This project builds a web application using Django (back-end) and Bootstrap (front-end) to empower students, faculty, administrators, and the college management team.

## Features

### A Single Platform for All Your College Needs

#### Faculty:
- Effortlessly manage student progress with features like:
  - Updating marks
  - Updating attendance
  - Making announcements for students

#### Students:
- Stay organized and informed with functionalities like:
  - Accessing grades and attendance
  - Downloading hall-tickets and fee receipts
  - Viewing course syllabus and subjects

#### Accounts Department:
- Maintain financial transparency through:
  - Verifying student transactions
  - Generating fee receipts

#### Head of Department:
- Foster a vibrant campus life by:
  - Adding details of cultural and academic clubs

### User-Centric Design for a Seamless Experience
- **Personalized Dashboards:** Access essential information at a glance.
- **Secure Access:** Manage personal data and update preferences with confidence.

### Built with Modern Technologies
- **Django:** A robust framework for efficient development.
- **Bootstrap:** A responsive framework for a user-friendly interface.

## Getting Started

Installation
Clone the repository:
```
git clone https://github.com/your-username/college-management-system.git
```
Navigate to the project directory:
```
cd college-management-system
```
Create a virtual environment:
```
python -m venv env
```
Activate the virtual environment:
On Windows:
```
.\env\Scripts\activate
```
On macOS and Linux:
```
source env/bin/activate
```
Install the required dependencies:
```
# Install Django
pip install Django

# Install Pillow
pip install Pillow

# Install ReportLab
pip install reportlab
```
Apply the migrations and run the development server:
```
python manage.py migrate
python manage.py runserver
```
Open your web browser and go to http://localhost:8000/
