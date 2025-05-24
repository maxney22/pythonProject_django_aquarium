from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

from django import forms

class Formulaire(ModelForm):
    class Meta:
        model = models.DataBase
        fields = ('nom', 'taille', 'duree_de_vie','environnement' )
        labels = {
            'nom' : _('Nom'),
            'taille' : _('taille en cm') ,
            'duree_de_vie' : _('durée de vie (en année)'),
            'environnement' : _('environnement'),
        }
