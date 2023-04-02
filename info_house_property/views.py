from django.shortcuts import render,  get_object_or_404, redirect
from . forms import InfoHousePropertyForm
from .models import InfoHouseProperty

# Create your views here.
def create(request):
    form = InfoHousePropertyForm()
    if request.method == "POST":
        form = InfoHousePropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_hp_read')
    context = {
        'form':form
    }
    return render(request, 'info_house_property/create.html', context)

# Read 
def info_hp_read(request):
    info_hp_data = InfoHouseProperty.objects.all()
    context = {
        'info_hp_data': info_hp_data
    }
    return render(request, 'info_house_property/read.html', context)

# Update 
def info_hp_update(request, pk):
    get_info_hp_data = get_object_or_404(InfoHouseProperty, pk=pk)
    form = InfoHousePropertyForm(instance=get_info_hp_data)
    if request.method == "POST":
        form = InfoHousePropertyForm(request.POST, instance=get_info_hp_data)
        if form.is_valid():
            form.save()
            return redirect('info_hp_read')
    context = {
        'form':form
    }
    return render(request, 'info_house_property/update.html', context)

# Delete 
def info_hp_delete(reqest, pk):
    get_info_hp = get_object_or_404(InfoHouseProperty, pk=pk)
    get_info_hp.delete()
    return redirect('info_hp_read')