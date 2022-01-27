from django import forms
from .models import Etudiant,Note

class EtudiantForms(forms.ModelForm):
    class Meta :
        model = Etudiant
        fields = '__all__'
        widgets = {
            'nom_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'prenom_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'matricule_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'cin_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'date_nai_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'adresse_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'tel_etudiant' :forms.TextInput(attrs={'class' : 'form-control'}),
            'classe' :forms.Select(attrs={'class' : 'form-control'}),
            'sex' :forms.Select(attrs={'class' : 'form-control'})
        }
class NoteForms(forms.ModelForm):
    class Meta :
        model = Note
        fields = ['Note_devoir','Note_examen','etudiant','matiere']
        widgets = {
            'Note_devoir' :forms.TextInput(attrs={'class' : 'form-control'}),
            'Note_examen' :forms.TextInput(attrs={'class' : 'form-control'}),
            'etudiant' :forms.Select(attrs={'class' : 'form-control'}),
            'matiere' :forms.Select(attrs={'class' : 'form-control'}),           
        }