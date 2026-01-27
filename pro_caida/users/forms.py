from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Submit, Column, Fieldset

from .models import Hermano

class HermanoForm(forms.ModelForm):
    
    class Meta:
        model = Hermano
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configuracion básica de cristpy
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'    
        
        # Layout
        self.helper.layout = Layout(
            Fieldset(
                'Información Personal',
            Row(
                Column('dni', css_class='col-md-6'),
                Column('nombre', css_class='col-md-6'),
            ),
            Row(
                Column('apellido1', css_class='col-md-6'),
                Column('apellido2', css_class='col-md-6'),
            ),
                Row(
                    Column('fec_nacimiento', css_class='col-md-6'),
                    Column('email', css_class='col-md-6'),
                )
            ),
            Fieldset(
                'Información de Hermano',
                Row(
                    Column('numero_hermano', css_class='col-md-4'),
                    Column('tipo_hermano', css_class='col-md-4'),
                    Column('cargo_junta', css_class='col-md-4'),
                ),
            )
        )
