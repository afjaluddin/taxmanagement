from django.shortcuts import render,  get_object_or_404, redirect
from . forms import InfoAgricaltureForm
from .models import InfoAgricalture

# Create your views here.
def create(request):
    form = InfoAgricaltureForm()
    if request.method == "POST":
        form = InfoAgricaltureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_agri_read')
    context = {
        'form':form
    }
    return render(request, 'info_agricalture/create.html', context)

# Read 
def info_agri_read(request):
    info_agri_data = InfoAgricalture.objects.all()
    context = {
        'info_agri_data': info_agri_data
    }
    return render(request, 'info_agricalture/read.html', context)

# Update 
def info_agri_update(request, pk):
    get_info_agri_data = get_object_or_404(InfoAgricalture, pk=pk)
    form = InfoAgricaltureForm(instance=get_info_agri_data)
    if request.method == "POST":
        form = InfoAgricaltureForm(request.POST, instance=get_info_agri_data)
        if form.is_valid():
            form.save()
            return redirect('info_agri_read')
    context = {
        'form':form
    }
    return render(request, 'info_agricalture/update.html', context)

# Delete 
def info_agri_delete(reqest, pk):
    get_info_agri = get_object_or_404(InfoAgricalture, pk=pk)
    get_info_agri.delete()
    return redirect('info_agri_read')