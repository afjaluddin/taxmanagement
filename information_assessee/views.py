from django.shortcuts import render,  get_object_or_404, redirect
from . forms import InformationAssesseeForm
from .models import InformationAssessee
# Create your views here.

def create(request):
    form = InformationAssesseeForm()
    if request.method == "POST":
        form = InformationAssesseeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    context = {
        'form':form
    }
    return render(request, 'information_assessee/create.html', context)

# Read 
def info_ssessee_read(request):
    info_ssessee_data = InformationAssessee.objects.all()
    context = {
        'info_ssessee_data': info_ssessee_data
    }
    return render(request, 'information_assessee/read.html', context)

# Update 
def info_ssessee_update(request, pk):
    get_info_ssessee_data = get_object_or_404(InformationAssessee, pk=pk)
    form = InformationAssesseeForm(instance=get_info_ssessee_data)
    if request.method == "POST":
        form = InformationAssesseeForm(request.POST, instance=get_info_ssessee_data)
        if form.is_valid():
            form.save()
            return redirect('info_ssessee_read')
    context = {
        'form':form
    }
    return render(request, 'information_assessee/update.html', context)


# Delete 
def info_ssessee_delete(reqest, pk):
    get_info_ssessee = get_object_or_404(InformationAssessee, pk=pk)
    get_info_ssessee.delete()
    return redirect('info_ssessee_read')