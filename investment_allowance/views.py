from django.shortcuts import render,  get_object_or_404, redirect
from .forms import InvestmentAllowanceForm
from .models import InvestmentAllowance
# Create your views here.

def create(request):
    form = InvestmentAllowanceForm()
    if request.method == "POST":
        form = InvestmentAllowanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investment_allowance_read')
    context = {
        'form':form
    }
    return render(request, 'investment_allowance/create.html', context)

# Read 
def investment_allowance_read(request):
    investment_allowance_data = InvestmentAllowance.objects.all()
    context = {
        'investment_allowance_data': investment_allowance_data
    }
    return render(request, 'investment_allowance/read.html', context)

# Update 
def investment_allowance_update(request, pk):
    get_investment_allowance_data = get_object_or_404(InvestmentAllowance, pk=pk)
    form = InvestmentAllowanceForm(instance=get_investment_allowance_data)
    if request.method == "POST":
        form = InvestmentAllowanceForm(request.POST, instance=get_investment_allowance_data)
        if form.is_valid():
            form.save()
            return redirect('investment_allowance_read')
    context = {
        'form':form
    }
    return render(request, 'investment_allowance/update.html', context)

# Delete 
def investment_allowance_delete(reqest, pk):
    get_investment_allowance = get_object_or_404(InvestmentAllowance, pk=pk)
    get_investment_allowance.delete()
    return redirect('investment_allowance_read')