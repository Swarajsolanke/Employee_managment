from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Role, Employee,Contact
from datetime import datetime
from django.db.models import Q
# Create your views here.
def home(req):
    return render(req,'index.html')

def about(req):
    return render(req,'aboutus.html')

def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        subject=req.POST['subject']
        message=req.POST['message']
        if name and email and subject and message:
            contact=Contact( name=name,email=email, subject=subject, message=message)
            contact.save()
            return HttpResponse("Thank for contacting us, we will get back to you soon.")
        else:
            return HttpResponse("please fill all the fields")
    elif req.method=='GET':
        return render(req,'contact.html')
    else:
        return HttpResponse("inavlid request: kindly try again")
def job(req):
    return render(req,'job.html')
def privacy(req):
    return render(req,'privacy.html')

def view_employ(req):
    emps=Employee.objects.all()
    print(emps)
    context={
        'emp':emps
    }
    print(context)
    return render(req,'view_employ.html',context)

def add_employ(req):
    if req.method=="POST":
        first_name=req.POST['first_name']
        last_name=req.POST["last_name"]
        salary=int(req.POST["salary"])
        dept=int(req.POST['dept'])
        role=int(req.POST['role'])
        #bonus=int(req.POST['bonus'])
        phone=int(req.POST['phone'])
        
        emp=Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            dept_id=dept,
            role_id=role,
            #bouns=bonus,
            phone=phone,
            hire_date=datetime.now()
        )
        emp.save()
        return HttpResponse("Sucessfully added ")

    elif req.method=='GET':
        return render(req,"add_employ.html")
    else:
        return HttpResponse("sucessfully added employee")
    

def delete_employ(req,emp_id=0):
    if emp_id:
        try:
            emp_to_removed=Employee.objects.get(id=emp_id)
            emp_to_removed.delete()
            return HttpResponse("Employee removed successfully")
        except Exception as e:
            return HttpResponse(f"Error:{e}")
        

    
    emp=Employee.objects.all()
    context={
        "emp":emp
    }
    return render(req,'remove_employ.html',context)

def Filter_employ(req):
    if req.method=="POST":
        name=req.POST["name"]
        dept=req.POST["dept"]
        role=req.POST["role"]
        emps=Employee.objects.all()
        print(emps)
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q (last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
            "emp":emps
        }
        return render(req,"view_employ.html",context)
    elif req.method=="GET":
        return render(req,'filter_employ.html')
    else:
        return HttpResponse("Kindly Search available Employee")
