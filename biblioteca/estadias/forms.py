from django import forms
from .models import model_estadias

class estadias_form(forms.ModelForm):

    carrera_choice = [
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
        ("LGCH","LGCH")
        ]

    proyecto = forms.CharField(label='Proyecto', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre del proyecto'}))
    matricula = forms.IntegerField(label='Matricula', required=True, widget=forms.NumberInput (attrs={'class':'form-control','placeholder':'Ingrese la matricula del alumno'}))
    alumno = forms.CharField(label='Alumno', required=False, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre del alumno'}))
    asesor_academico = forms.CharField(label='Asesor académico', required=False, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Indique el asesor académico'}))
    generacion = forms.CharField(label='Generación', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Indique la generación'}))
    empresa = forms.CharField(label='Empresa', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre de la empresa'}))
    asesor_orga = forms.CharField(label='Asesor Institucional', required=False, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el asesor organizacional'}))
    carrera = forms.ChoiceField(label='Carrera', choices=carrera_choice, required=True, widget=forms.Select (attrs={'class':'form-control','placeholder':'Indique la carrera'}))
    reporte = forms.FileField(label='Reporte', required=True, widget=forms.FileInput(attrs={'class':'form-control', 'accept':'.pdf', 'placeholder':'Ingrese reporte en formato PDF'}))
    class Meta:
        model = model_estadias
        fields = ('proyecto', 'matricula','alumno','asesor_academico','generacion','empresa','asesor_orga','carrera', 'reporte')