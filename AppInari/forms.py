from django import forms

class ClienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.IntegerField()
