from django.db import models

# Create your models here.
class TypePose(models.Model):
    nom = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Routes(models.Model):
    code = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Longitude(models.Model):
    degre = models.IntegerField()
    minute = models.IntegerField()
    seconde = models.IntegerField()
    fuseau = models.CharField(max_length=10)

    def __str__(self):
        return str(self.degre)

class Latitude(models.Model):
    degre = models.IntegerField()
    minute = models.IntegerField()
    seconde = models.IntegerField()
    fuseau = models.CharField(max_length=10)

    def __str__(self):
        return str(self.degre)

class TypeIncident(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code

class SystemDeclenchement(models.Model):
    nom = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom
    
class TypeSystem(models.Model):
    nom = models.CharField(max_length=100, null=True)
    system_declenchement = models.ForeignKey(SystemDeclenchement, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom


class CaracteristiquePoints(models.Model):
    nom = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
    
    
class Eei(models.Model):
    nom = models.CharField(max_length=200)
    date = models.DateField()
    details = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    type_pose = models.ForeignKey(TypePose, on_delete=models.CASCADE)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    longitude = models.ForeignKey(Longitude, on_delete=models.CASCADE)
    latitude = models.ForeignKey(Latitude, on_delete=models.CASCADE)
    type_incident = models.ForeignKey(TypeIncident, on_delete=models.CASCADE)
    type_system = models.ForeignKey(TypeSystem, on_delete=models.CASCADE, null=True)
    caracteristique = models.ForeignKey(CaracteristiquePoints, on_delete=models.CASCADE)

    def __str__(self):
        return f"Eei {self.id} - {self.date.strftime('%Y-%m-%d')} - {self.nom}"



    