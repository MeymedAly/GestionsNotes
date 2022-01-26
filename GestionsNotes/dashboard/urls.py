from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("", views.index, name="dashboard"),
    path("etudiant/", views.etudiant, name="liste-etudient"),
    path("modifier/<int:id>/", views.modifEtidiant, name="modifier"),
    path("supprimer/<int:id>/", views.suppEtidiant, name="supprimer"),
    path("geologie/", views.geologie, name="geologie"),
    path("statistique-etudiants/", views.statistique_etudiants, name="statistique-etudiants"),

  
]