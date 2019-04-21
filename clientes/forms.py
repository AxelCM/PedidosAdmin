from django import forms
from clientes.models import Cliente


#Formulario para Registrar un cliente nuevo
class RegisterClientForm(forms.ModelForm):

    class Meta:

        model = Cliente
        fields = (
        'n_representante',
        'nombre_comercial',
        'telefono',
        'direccion',
        'mayorista',
        'email',
        'nit',
        )

#Funcion Para Validar que todos los datos del formulario HTML esten correctos
    def save(self):

#Validando datos y creando el objecto cliente.objects.create()

        n_representante = self.cleaned_data['n_representante']
        nombre_comercial = self.cleaned_data['nombre_comercial']
        telefono = self.cleaned_data['telefono']
        direccion = self.cleaned_data['direccion']
        mayorista = self.cleaned_data['mayorista']
        email = self.cleaned_data['email']
        nit = self.cleaned_data['nit']
        cliente = Cliente.objects.create(
        n_representante=n_representante ,
        nombre_comercial=nombre_comercial ,
        telefono=telefono,
        direccion=direccion,
        mayorista=mayorista,
        email=email,
        nit=nit
        )
        cliente.save()
