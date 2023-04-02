from django.shortcuts import render,  get_object_or_404, redirect
from . forms import InformationSalaryForm
from .models import InformationSalary
# Create your views here.

def create(request):
    form = InformationSalaryForm()
    if request.method == "POST":
        form = InformationSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_salary_read')
    context = {
        'form':form
    }
    return render(request, 'information_salary/create.html', context)

# Read 
def info_salary_read(request):
    info_salary_data = InformationSalary.objects.all()
    context = {
        'info_salary_data': info_salary_data
    }
    return render(request, 'information_salary/read.html', context)

# Update 
def info_salary_update(request, pk):
    get_info_salary_data = get_object_or_404(InformationSalary, pk=pk)
    form = InformationSalaryForm(instance=get_info_salary_data)
    if request.method == "POST":
        form = InformationSalaryForm(request.POST, instance=get_info_salary_data)
        if form.is_valid():
            form.save()
            return redirect('info_salary_read')
    context = {
        'form':form
    }
    return render(request, 'information_salary/update.html', context)

# Delete 
def info_salary_delete(reqest, pk):
    get_info_salary = get_object_or_404(InformationSalary, pk=pk)
    get_info_salary.delete()
    return redirect('info_salary_read')