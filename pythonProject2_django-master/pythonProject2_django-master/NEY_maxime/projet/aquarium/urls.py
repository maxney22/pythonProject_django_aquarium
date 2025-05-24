from django.urls import path

from . import views

urlpatterns = [
    path("ROUTE_no_VUE/", views.ACTION_no_VUE),
    path("", views. ACTION_statique_accueil),
    path("ROUTE_formulaire/", views.ACTION_formulaire),
    path("ROUTE_traitement/", views.ACTION_traitement),
    path("ROUTE_afficher_all/", views.ACTION_afficher_all),
    path("ROUTE_afficher_one/<int:id>/", views.ACTION_afficher_one),
    path("ROUTE_modifier/<int:id>/", views.ACTION_modifier),
    path("ROUTE_sauvegarder_modif/<int:id>/", views.ACTION_sauvegarder_modif),
    path("ROUTE_supprimer/<int:id>/", views.ACTION_supprimer, name='ROUTE_supprimer'),
]