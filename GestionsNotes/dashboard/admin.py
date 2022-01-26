from django.contrib import admin
from .models import Classe,Module,Matiere,Etudiant,Specialite,Note
# Register your models here.
class EtudiantAdmin(admin.ModelAdmin):
    fields = ('nom_etudiant','prenom_etudiant','matricule_etudiant','cin_etudiant','date_nai_etudiant','adresse_etudiant','tel_etudiant','classe','sex')
    list_display = ('nom_etudiant','prenom_etudiant','matricule_etudiant','cin_etudiant','date_nai_etudiant','adresse_etudiant','tel_etudiant','sex')

class ClasseAdmin(admin.ModelAdmin):
    fields = ('nom_classe','niveau_classe')
    list_display = ('nom_classe','niveau_classe')

class ModuleAdmin(admin.ModelAdmin):
    fields = ('nom_module','coiffi_module','classe')
    list_display = ('nom_module','coiffi_module')

class MatiereAdmin(admin.ModelAdmin):
    fields = ('nom_matiere','coiffi_matiere','module')
    list_display = ('nom_matiere','coiffi_matiere')



admin.site.register(Classe,ClasseAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Matiere,MatiereAdmin)
admin.site.register(Etudiant,EtudiantAdmin)
admin.site.register(Specialite)
admin.site.register(Note)

