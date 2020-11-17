from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# ----------------------------------------------------------------------------------------------------------------------
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            em = fm.cleaned_data['Email']
            pw = fm.cleaned_data['Password']
            reg = User(Name=nm, Email=em, Password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    data = User.objects.all()
    return render(request, 'Enroll/addandshow.html', {'form': fm, 'data': data})


# ----------------------------------------------------------------------------------------------------------------------
def delete_data(request, id):
    if request.method == 'POST':
        dl = User.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')


# ----------------------------------------------------------------------------------------------------------------------
def update_view(request, id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up = User.objects.get(pk=id)
        fm = StudentRegistration(instance=up)
    return render(request, 'Enroll/update.html', {'form': fm, 'id': id})
# ----------------------------------------------------------------------------------------------------------------------
