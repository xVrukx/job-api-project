from django.urls import path
from . import views

urlpatterns = [
    path('api/create-company/', views.create_company),
    path('api/post-job/', views.post_job),
    path('api/jobs/', views.job_list),
    path('api/apply/', views.apply_job),
    path('api/applicants/<int:job_id>/', views.job_applicants),
]