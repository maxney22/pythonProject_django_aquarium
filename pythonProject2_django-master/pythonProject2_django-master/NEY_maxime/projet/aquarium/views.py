from django.shortcuts import render
from . import models
from django.shortcuts import HttpResponse

from django.http import HttpResponseRedirect
from .forms import Formulaire

def ACTION_no_VUE (request):
    return HttpResponse("Bienvenue sur la page associée à l’ACTION_no_VUE !")

def ACTION_statique_accueil(request):
    return render(request, "aquarium/VUE_statique_accueil.html")

def ACTION_formulaire(request):
    formulaire_vide = Formulaire()
    return render(request, "aquarium/VUE_formulaire.html", {"formulaire": formulaire_vide})

def ACTION_traitement(request):
    formulaire_plein = Formulaire(request.POST)
    if formulaire_plein.is_valid():
        sauvegarde = formulaire_plein.save()
        return render(request, "aquarium/VUE_traitement.html", {"donnees": sauvegarde})
    else:
        return render(request, "aquarium/VUE_formulaire.html", {"formulaire": formulaire_plein})

def ACTION_afficher_all(request):
    liste_data = list(models.DataBase.objects.all())
    return render(request, "aquarium/VUE_afficher_all.html", {"liste": liste_data})

def ACTION_afficher_one(request, id):
    data = models.DataBase.objects.get(pk=id)
    return render(request, "aquarium/VUE_traitement.html", {"donnees": data, "id": id})

def ACTION_modifier(request, id):
    data = models.DataBase.objects.get(pk=id)
    dico = data.make_dico()
    formulaire_avant_modif = Formulaire(dico)
    return render(request, "aquarium/VUE_formulaire.html", {"formulaire": formulaire_avant_modif, "id": id})

def ACTION_sauvegarder_modif(request, id):
    formulaire_avec_modif = Formulaire(request.POST)
    if formulaire_avec_modif.is_valid():
        sauvegarde = formulaire_avec_modif.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        return HttpResponseRedirect("aquarium/ROUTE_afficher_all/")
    else:
        return render(request, "aquarium/VUE_formulaire.html", {"formulaire": formulaire_avec_modif, "id": id})


def ACTION_supprimer(request, id):
    data = models.DataBase.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect("/aquarium/ROUTE_afficher_all/")