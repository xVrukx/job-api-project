import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, JobPost,Applicant

@csrf_exempt
def create_company(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            location = data.get("location")
            description = data.get("description")

            if not all([name, location, description]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            company = Company.objects.create(name=name, location=location, description=description)
            return JsonResponse({"message": "Company created successfully", "company_id": company.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)


@csrf_exempt
def post_job(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            company_id = data.get("company_id")
            title = data.get("title")
            description = data.get("description")
            salary = data.get("salary")
            location = data.get("location")

            if not all([company_id, title, description, salary, location]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            try:
                company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                return JsonResponse({"error": "Company not found"}, status=404)

            job = JobPost.objects.create(
                company=company,
                title=title,
                description=description,
                salary=salary,
                location=location
            )

            return JsonResponse({"message": "Job posted successfully", "job_id": job.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def job_list(request):
    if request.method == "GET":
        jobs = JobPost.objects.select_related("company").all()
        job_data = []
        for job in jobs:
            job_data.append({
                "id": job.id,
                "title": job.title,
                "description": job.description,
                "salary": job.salary,
                "location": job.location,
                "created_at": job.created_at.strftime("%Y-%m-%d %H:%M"),
                "company": {
                    "id": job.company.id,
                    "name": job.company.name,
                    "location": job.company.location,
                }
            })
        return JsonResponse(job_data, safe=False)
    else:
        return JsonResponse({"error": "Only GET method is allowed"}, status=405)
    
@csrf_exempt
def apply_job(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            resume_link = data.get("resume_link")
            job_id = data.get("job_id")

            if not all([name, email, resume_link, job_id]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            try:
                job = JobPost.objects.get(id=job_id)
            except JobPost.DoesNotExist:
                return JsonResponse({"error": "Job not found"}, status=404)

            applicant = Applicant.objects.create(
                name=name,
                email=email,
                resume_link=resume_link,
                job=job
            )

            return JsonResponse({"message": "Application submitted", "applicant_id": applicant.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def job_applicants(request, job_id):
    if request.method == "GET":
        try:
            job = JobPost.objects.get(id=job_id)
        except JobPost.DoesNotExist:
            return JsonResponse({"error": "Job not found"}, status=404)

        applicants = Applicant.objects.filter(job=job)
        applicant_data = []
        for a in applicants:
            applicant_data.append({
                "id": a.id,
                "name": a.name,
                "email": a.email,
                "resume_link": a.resume_link,
                "applied_at": a.applied_at.strftime("%Y-%m-%d %H:%M")
            })

        return JsonResponse(applicant_data, safe=False)
    else:
        return JsonResponse({"error": "Only GET method is allowed"}, status=405)
