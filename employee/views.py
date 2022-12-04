from django.shortcuts import render, redirect
from .models import Employee
from employee.forms import SaveEmployee
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    employee = Employee.objects 
    if request.method == 'POST':
        form = SaveEmployee(request.POST or None)
        if form.is_valid():
            form.save() 
            messages.success(request,("Employee details added successfully"))
            return redirect('../../employee')
    else:
        return render(request, 'index.html', {'employee': employee})
@login_required
def delete(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    messages.success(request,("Employee details deleted successfully"))
    return redirect('../../employee')
@login_required
def edit(request, employee_id):
    if request.method == "POST":
        employee = Employee.objects.get(pk=employee_id) 
        form = SaveEmployee(request.POST or None, instance = employee)
        if form.is_valid():
            form.save()
            messages.success(request,("Employee details updated successfully"))

        return redirect('../../employee')

    else:
            employee = Employee.objects.get(pk=employee_id)
            return render(request, 'edit.html', {'employee': employee}) 



