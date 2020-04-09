from django.db import models
from PIL import Image
from django.utils import timezone

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
  
            
class Oglas(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    slika = models.ImageField(default=None)
    naslov = models.CharField(max_length = 100)
    date = models.DateTimeField(default = timezone.now)
    ODECA_MUSKA = 'OM'
    OBUCA_MUSKA ='BM'
    ODECA_ZENSKA = 'OZ'
    OBUCA_ZENSKA ='BZ'
    KNJIGE_SKOLSKE = 'KS'
    KNJIGE_OSTALE = 'KO'
    IGRACKE = 'IG'
    TEHNIKA = 'TE'
    RUKOTVORINE = 'RK'
    IZBOR_KATEGORIJA = [(ODECA_MUSKA, 'Odeca Muska'),(ODECA_ZENSKA, 'Odeca Zenska'), 
                        (OBUCA_MUSKA, 'Obuca Muska'),(OBUCA_ZENSKA, 'Obuca Zenska'),
                        (KNJIGE_SKOLSKE, 'Knjige Skolske'), (KNJIGE_OSTALE, 'Knjige Ostale'),
                        (IGRACKE, 'Igracke'), (TEHNIKA,'Tehnika'), 
                        (RUKOTVORINE, 'Rukotvorine')] 
    kategorija = models.CharField(max_length = 2, choices=IZBOR_KATEGORIJA, default=KNJIGE_SKOLSKE)
    
    stanje = models.CharField(max_length = 100)
    
    cena = models.IntegerField()
    opis = models.TextField(default= None)
    
    
    def __str__(self):
        return self.naslov
    
    def save(self):
        super().save()
        
        img = Image.open(self.slika.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.slika.path)

class Image(models.Model):
    img = models.ImageField(default=None)
    oglas = models.ForeignKey(Oglas, on_delete=models.CASCADE)
    