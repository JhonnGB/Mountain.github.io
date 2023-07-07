from django import forms

class PedidosForm(forms.Form):
    name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder':'Escriba su email'}),min_length=3, max_length=100)
    telefono = forms.CharField(label='Teléfono', required=True , widget=forms.TextInput(attrs={'placeholder': 'Escribe tu telefono'}))
    entregas = forms.CharField(label="Forma de entrega", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Domicilio/Ir la lugar'}))
    direccion = forms.CharField(label="Direccion", required=True, widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Mz a casa 10 barrio/montecarlo'}))
    indicaciones = forms.CharField(label="Indicaciones", required=False, widget=forms.TextInput(attrs={'placeholder': 'Torre 4, Apartamento 604'}))
    pagos = forms.CharField(label="Forma de pago", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nequi/Efectivo'}))

    