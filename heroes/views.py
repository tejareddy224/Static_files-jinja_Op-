from django.shortcuts import render

# Create your views here.
def allu(request):
    return render(request,'allu.html')
def ram(request):
    return render(request,'ram.html')
def ntr(request):
    return render(request,'ntr.html')