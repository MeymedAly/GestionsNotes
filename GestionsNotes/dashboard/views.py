from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from .forms import NoteForms,EtudiantForms
from django.http import JsonResponse
from django.core import serializers
# Create your views here.



#def pivot_data(request):
#    dataset = Etudiant.objects.all()
#    data = serializers.serialize('json', dataset)
#    return JsonResponse(data, safe=False)

def login(request):
    return render(request, 'dashboard/authentication-login.html')


def index(request):
    return render(request, 'dashboard/index.html')

def note(request):
    context ={
       # 'notes' : Note.objects.all(),
        'forms' : NoteForms(),
    }
    return render(request, 'dashboard/note.html',context)




def modifEtidiant(request,id):
    etudiant_id = Etudiant.objects.get(id=id)
    if request.method =='POST':
        etudiant_save = EtudiantForms(request.POST,request.FILES,instance=etudiant_id)
        if etudiant_save.is_valid():
            etudiant_save.save()
            return redirect('/etudiant')
    else:
        etudiant_save = EtudiantForms(instance=etudiant_id)
        context = {
            'forms':etudiant_save,
        }
    return render(request, "dashboard/modifierEtudiant.html",context)


def suppEtidiant(request,id):
    etudiant_supp = Etudiant.objects.get(id=id)
    if request.method =='POST':
        etudiant_supp.delete()
        return redirect('/')
    return render(request,"dashboard/suprimerEtudiant.html")

def etudiant(request):
    if request.method == 'POST':
        ajout_etudiant = EtudiantForms(request.POST)
        if ajout_etudiant.is_valid():
            ajout_etudiant.save()
    context ={
        'etudiants' : Etudiant.objects.all(),
        'form' : EtudiantForms(),
    }
    return render(request, "dashboard/etudiant.html", context)





def elements(request):
    return render(request, "dashboard/elements.html")
