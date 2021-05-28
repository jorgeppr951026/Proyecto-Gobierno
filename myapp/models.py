from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Topado(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Flores(models.Model):
    um_choince = [('uno','Uno'),('docena','Docena')]
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    um = models.CharField(max_length=10, choices=um_choince,)
    precio_1 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_3 = models.DecimalField(max_digits=10, decimal_places=2)
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)
    
    class Meta:
        unique_together = (('descripcion', 'topado_por','um' ),)

    def __str__(self):
        return self.descripcion


class Coronas(models.Model):
    variedades_de_flores = models.CharField(max_length=200)
    cant_docenas = models.CharField(max_length=200 , verbose_name="Cantidad de docenas")
    diametro_aro = models.CharField(max_length=200, verbose_name="Diámetro del aro")
    um = models.CharField(max_length=200)
    precio_minorista =  models.DecimalField(max_digits=10, decimal_places=2)
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)

    class Meta:
        unique_together = (('variedades_de_flores', 'topado_por'),)
    
    def __str__(self):
        return self.variedades_de_flores


class Construccion(models.Model):
    producto = models.CharField(max_length=200)    
    um = models.CharField(max_length=200)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)

    class Meta:
        unique_together = (('producto', 'topado_por'),)
    
    def __str__(self):
        return self.producto

class Transporte(models.Model):
    municipio_choince = [('Bejucal','Bejucal'),('San José','San José'),('Jaruco','Jaruco'),('Santa Cruz','Santa Cruz'),('Madruga','Madruga'),('Nueva Paz','Nueva Paz'),('San Nicolás','San Nicolás'),
                     ('Güines','Güines'),('Melena','Melena'),('Batabanó','Batabanó'),('Quivicán','Quivicán'),]
    municipio = models.CharField(max_length=20, choices=municipio_choince,)
    tramo = models.CharField(max_length=200)
    km = models.IntegerField(default=0)
    triciclo = models.IntegerField(default=0)
    auto = models.IntegerField(default=0)
    auto_y_jeep = models.IntegerField(default=0)
    panel_y_micro = models.IntegerField(default=0)
    camioneta = models.IntegerField(default=0)
    camino = models.IntegerField(default=0,verbose_name="Camión")
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)

    class Meta:
        unique_together = (('tramo', 'topado_por','municipio'),)
   
    def __str__(self):
        return self.municipio + ' - ' + self.tramo


class Agricultura(models.Model):
    tipo_choince = [('Viandas','Viandas'),('Hortalizas','Hortalizas'),('Otras Hortalizas','Otras Hortalizas'),('Citricos y Frutas','Citricos y Frutas'),('Granos','Granos'),]
    tipo = models.CharField(max_length=20, choices=tipo_choince,)
    producto = models.CharField(max_length=200)
    compra_productor = models.DecimalField(max_digits=10, decimal_places=2)
    venta_mayorista = models.DecimalField(max_digits=10, decimal_places=2) 
    venta_minorista = models.DecimalField(max_digits=10, decimal_places=2)
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)
    
    class Meta:
        unique_together = (('producto', 'topado_por'),)

    def __str__(self):
        return self.producto

class Cerdo(models.Model):
    producto = models.CharField(max_length=200)
    precio =  models.DecimalField(max_digits=10, decimal_places=2)
    topado_por = models.ForeignKey(Topado,on_delete=CASCADE, default=None,)
    
    class Meta:
        unique_together = (('producto', 'topado_por'),)
        
    def __str__(self):
        return self.producto










