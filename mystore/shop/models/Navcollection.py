from django.db import models

class Navcollection(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120,blank=False, null=False)
    button_text = models.CharField(max_length=60,blank=False, null=False)
    button_link = models.CharField(max_length=255,blank=False, null=False)
    image = models.ImageField(upload_to="nav_collections", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #affichage sous forme de chaine de caractère
        return self.title
