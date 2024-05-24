from django.db import models
class estadias(models.Model):

   proyecto=models.CharField(max_length=150)
   alumno=models.CharField(max_length=150)
   asesor_academico=models.CharField(max_length=150)
   generacion=models.CharField(max_length=12)
   empresa=models.CharField(max_length=150)
   asesor_empresarial=models.CharField(max_length=150)
   ELECCION_CARRERA = (
        ("ADC","ADC"),
        ("MET", "MET"),
        ("QAI", "QAI"),
        ("PIA", "PIA"),
        ("QAM", "QAM"),
        ("ERC","ERC"),
        ("IDGS","IDGS"),
        ("ITEA","ITEA"),
        ("IMET","IMET"),
        ("IER","IER"),
        ("ISIP","ISIP"),
        ("IPQ","IPQ"),
        ("LGCH","LGCH"))

   carrera=models.CharField(
        max_length=20,
        choices=ELECCION_CARRERA,
        default='2',
        blank=True,
        help_text="Prioridad de la tarea"
    )

   reporte = models.FileField(null=True,upload_to='files',blank=True)
   convenio = models.FileField(null=True,upload_to='files',blank=True)
   c_aceptacion= models.FileField(null=True,upload_to='files',blank=True)
   cronograma= models.FileField(null=True,upload_to='files',blank=True)







   def _str_(self):
        return self.alumno

   class Meta:
        verbose_name="estadias"
        verbose_name_plural='estadias'

