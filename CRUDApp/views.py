from django.shortcuts import render, redirect
from . import models, forms
from django.contrib import messages


# Create your views here.

# showemp method display all records of employee table
def showemp(request):
    showall = models.EmpModel.objects.all()
    return render(request, 'CRUDApp/index.html', {"data": showall})


# insertemp method helps to insert new record in employee table
def insertemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and request.POST.get('gender') and request.POST.get(
                'email') and request.POST.get('occupation') and request.POST.get('salary'):
            saveRecord = models.EmpModel()
            saveRecord.empname = request.POST.get('empname')
            saveRecord.gender = request.POST.get('gender')
            saveRecord.email = request.POST.get('email')
            saveRecord.occupation = request.POST.get('occupation')
            saveRecord.salary = request.POST.get('salary')
            saveRecord.save()
            messages.success(request, 'Employee' + saveRecord.empname + 'Is saved successfully')
            return render(request, 'CRUDApp/insert.html')
        else:
            messages.success(request, 'Text field are empty')
            return render(request, 'CRUDApp/insert.html')
    else:
        return render(request, 'CRUDApp/insert.html')


# edit temp function helps to edits users details according to user id
def edittemp(request, id):
    edittempobj = models.EmpModel.objects.get(id=id)
    return render(request, 'CRUDApp/edit.html', {"EmpModel": edittempobj})


# update temp function update the users detail according to users id
def updatetemp(request, id):
    updateemp = models.EmpModel.objects.get(id=id)
    form = forms.EmpForms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Updated Successfully.. !")
        return render(request, 'CRUDApp/edit.html', {"EmpModel": updateemp})


# delete function removes users from database according to user id
def deleteemp(request, id):
    deleteuser = models.EmpModel.objects.get(id=id)
    deleteuser.delete()
    showdata = models.EmpModel.objects.all()
    return render(request, 'CRUDApp/index.html', {"data": showdata})
