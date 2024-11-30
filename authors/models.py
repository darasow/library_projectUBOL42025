import os
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    biography = models.TextField()

    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)

    image = models.ImageField(upload_to='authors/images/', blank=True, null=True) # Ajout de champ image

    def save(self, *args, **kwargs):
        if not self.pk: # Si l'objet est en train d'être créé
            self.created_at = timezone.now()
            self.modified_at = None
        else:
            self.modified_at = timezone.now()
        super(Author, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Supprime l'image associée avant de supprimer l'objet
        if self.image:
            if os.path.isfile(self.image.path):
               os.remove(self.image.path)
        super(Author, self).delete(*args, **kwargs)

def __str__(self):
    return self.name