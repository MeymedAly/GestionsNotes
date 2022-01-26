from django.db import models

# Create your models here.


from django import forms
# Create your models here.

class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    nom_classe = models.CharField( max_length=100)
    niveau_classe = models.CharField( max_length=100)

    def __str__(self):
        return self.nom_classe

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    nom_module = models.CharField( max_length=100)
    coiffi_module = models.CharField( max_length=100)
    classe= models.ForeignKey(Classe,  on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nom_module 



class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    nom_matiere = models.CharField( max_length=100)
    coiffi_matiere = models.CharField( max_length=100)
    #note_devoir = models.CharField( max_length=100)
    #note_exemen = models.CharField( max_length=100)
    module= models.ForeignKey(Module,  on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nom_matiere 


class Etudiant(models.Model):
    sex_etudiant = [
        ('M','M'),
        ('F','F'),
    ]

    id = models.AutoField(primary_key=True)
    nom_etudiant = models.CharField( max_length=100)
    prenom_etudiant = models.CharField( max_length=100)
    matricule_etudiant = models.CharField( max_length=100)
    cin_etudiant = models.CharField( max_length=50)
    date_nai_etudiant = models.CharField( max_length=100)
    adresse_etudiant = models.CharField( max_length=100)
    tel_etudiant = models.CharField( max_length=100)
    #id_resultat_etudiant  = models.ForeignKey( max_length=50)
    classe = models.ForeignKey(Classe,  on_delete=models.CASCADE)
    sex = models.CharField( max_length=50, choices=sex_etudiant)
    def __str__(self):
        return self.nom_etudiant


class Resultat(models.Model):
    id = models.AutoField(primary_key=True)
    moyen_general = models.FloatField(default=0)
    etudiant= models.ForeignKey(Etudiant,on_delete=models.CASCADE)

class Specialite(models.Model):
    id = models.AutoField(primary_key=True)
    nom_specialite = models.CharField( max_length=100)
    classe= models.ForeignKey(Classe,  on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nom_specialite    

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    Note_devoir = models.FloatField(default=0)
    Note_examen = models.FloatField(default=0)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere= models.ForeignKey(Matiere,on_delete=models.CASCADE)
    

#    def __str__(self):
#        return self.etudiant    


#class resultat(models.Model):
#    id_resultat= models.CharField( max_length=100)
#    moyn = models.CharField( max_length=100)


#    def __str__(self):
#        return self.moyn

   
 