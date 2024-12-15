from django.shortcuts import render
from .models import Person
import sqlite3
from django.http import HttpResponse

# Create your views here.


def main(request):
    if request.POST:
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
    return render(request,'index.html')


def foydalanuvchilar(request):
    conn = sqlite3.connect(r'D:\django_51_dars\db.sqlite3')
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM myapp_person
    """)
    a = cur.fetchall()
    print(a)
    return render(request,"ruyhat.html",context={"b":a})
    conn.close()
    cur.close()