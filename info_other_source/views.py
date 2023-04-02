from django.shortcuts import render,  get_object_or_404, redirect
from . forms import InfoOtherSourceForm
from .models import InfoOtherSource

# Create your views here.
def create(request):
    form = InfoOtherSourceForm()
    if request.method == "POST":
        form = InfoOtherSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_os_read')
    context = {
        'form':form
    }
    return render(request, 'info_other_source/create.html', context)

# Read 
def info_os_read(request):
    info_os_data = InfoOtherSource.objects.all()
    context = {
        'info_os_data': info_os_data
    }
    return render(request, 'info_other_source/read.html', context)

# Update 
def info_os_update(request, pk):
    get_info_os_data = get_object_or_404(InfoOtherSource, pk=pk)
    form = InfoOtherSourceForm(instance=get_info_os_data)
    if request.method == "POST":
        form = InfoOtherSourceForm(request.POST, instance=get_info_os_data)
        if form.is_valid():
            form.save()
            return redirect('info_os_read')
    context = {
        'form':form
    }
    return render(request, 'info_other_source/update.html', context)

# Delete 
def info_os_delete(reqest, pk):
    get_info_os = get_object_or_404(InfoOtherSource, pk=pk)
    get_info_os.delete()
    return redirect('info_os_read')