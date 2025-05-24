from django.db import models
import bleach


# Create your models here.

class Formulaire(models.Model):
    nom = models.CharField(max_length=100)
    taille = models.IntegerField(blank=False)
    duree_de_vie = models.IntegerField(blank=False)
    environnement = models.CharField(max_length=100)

    def __str__(self):
        str_retournee = f'<ul>'\
                       f'<li>Nom : <span>{self.nom}</span></li>' \
                       f'<li>taille :<span>{self.taille}</span></li>' \
                       f'<li>duree_de_vie :<span>{self.duree_de_vie}</span></li>' \
                       f'<li>environnement :<span>{self.environnement}</span></li>' \
                       f'</ul>'
        return bleach.clean(str_retournee, ["ul", "li", "span"], {})

class DataBase(models.Model):
    nom = models.CharField(max_length=100)
    taille = models.IntegerField(blank=False)
    duree_de_vie = models.IntegerField(blank=False)
    environnement = models.CharField(max_length=100)
    def make_dico(self):
        return {"nom": self.nom, "taille": self.taille, "duree_de_vie": self.duree_de_vie, "environnement": self.environnement }

    def __str__(self):
        return f"{self.nom} ({self.environnement}, {self.taille} cm, {self.duree_de_vie} ans)"

