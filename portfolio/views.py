from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    
    # Structural stream for your professional validations
    # Structural stream for your professional validations
    certifications = [
        {
            "title": "IBM AI Developer Professional Certificate", 
            "year": "2026", 
            "ref": "IBM_CRT_2026",
            "verify_link": "https://www.coursera.org/account/accomplishments/specialization/EEQTB2RIL5BB" 
        },
        {
            "title": "NPTEL - Internet of Things (IIT Kharagpur)", 
            "year": "2023", 
            "ref": "NPT_IOT_2023",
            "verify_link": None 
        }
    ]
    
    # Structural stream for your academic milestones
    education = [
        {
            "degree": "Master of Computer Applications (MCA)", 
            "uni": "APJ Abdul Kalam Technological University", 
            "year": "2023-2025"
        },
        {
            "degree": "Bachelor of Computer Applications (BCA)", 
            "uni": "University of Kerala", 
            "year": "2019-2022"
        }
    ]
    
    return render(request, 'portfolio/home.html', {
        'projects': projects, 
        'certs': certifications, 
        'edu': education
    })