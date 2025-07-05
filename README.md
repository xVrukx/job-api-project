🧰 Job Portal API (Without DRF)
A mini job portal backend built using core Django — no Django REST Framework (DRF). It allows companies to post jobs and applicants to apply via manual JsonResponse endpoints.

🔎 Objective
Create a backend system for:

Company registration

Job postings

Applicant submissions

Viewing job listings and applicants per job

🚀 Tech Stack
Python 3.x

Django (No DRF)

SQLite (default)

Function-Based Views

JSON Response (JsonResponse)

📦 Features
Feature	Endpoint	Method	Auth	Description
Create Company	/api/create-company/	POST	❌	Register a new company
Post a Job	/api/post-job/	POST	❌	Post a job for an existing company
List All Jobs	/api/jobs/	GET	❌	List all job posts with company names
Apply to Job	/api/apply/	POST	❌	Submit an application for a job
View Applicants	/api/applicants/<job_id>/	GET	❌	View all applicants for a specific job

🧱 Models
Company
Field	Type
name	CharField
location	CharField
description	TextField
created_at	DateTime

JobPost
Field	Type
company	FK → Company
title	CharField
description	TextField
salary	IntegerField
location	CharField
created_at	DateTime

Applicant
Field	Type
name	CharField
email	EmailField
resume_link	URLField
job	FK → JobPost
applied_at	DateTime

⚙️ Setup Instructions

# 1. Clone the repo
git clone <your-repo-url>
cd jobportal

# 2. Create a virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run the server
python manage.py runserver
🧪 Example API Requests
✅ POST /api/create-company/

{
  "name": "Google",
  "location": "Bangalore",
  "description": "Tech company"
}
✅ POST /api/post-job/

{
  "company_id": 1,
  "title": "Backend Developer",
  "description": "Experience with Django",
  "salary": 60000,
  "location": "Remote"
}
✅ GET /api/jobs/
✅ POST /api/apply/

{
  "name": "John Doe",
  "email": "john@doe.com",
  "resume_link": "https://example.com/resume.pdf",
  "job_id": 1
}
✅ GET /api/applicants/1/
⚠️ Constraints
❌ No DRF or Serializers

✅ Only JsonResponse and function-based views

✅ Proper error handling (e.g., missing fields, invalid IDs)

✅ SQLite used for DB
