"""
Form Schemas - Esquemas de dominio para todos los formularios
Capa de dominio - Definiciones de entidades
"""

schemas = {
    'cliente': {
        'title': 'Registro de Cliente',
        'name': 'registro-cliente',
        'path': 'registro-cliente',
        'components': [
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'RUT',
                'key': 'rut',
                'placeholder': 'Ej: 12345678-K',
                'persistent': True,
                'validate': {'required': True},
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Nombre',
                'key': 'nombre',
                'placeholder': '',
                'persistent': True,
                'validate': {'required': True},
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Apellido Paterno',
                'key': 'apellido_paterno',
                'placeholder': '',
                'persistent': True,
                'validate': {'required': True},
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Apellido Materno',
                'key': 'apellido_materno',
                'placeholder': '',
                'persistent': True,
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'email',
                'label': 'Email',
                'key': 'email',
                'placeholder': 'email@example.com',
                'persistent': True,
                'validate': {'required': True},
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'tel',
                'label': 'Teléfono',
                'key': 'telefono',
                'placeholder': '+56 9 XXXX XXXX',
                'persistent': True,
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Dirección',
                'key': 'direccion',
                'placeholder': '',
                'persistent': True,
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Ciudad',
                'key': 'ciudad',
                'placeholder': '',
                'persistent': True,
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Región',
                'key': 'region',
                'placeholder': '',
                'persistent': True,
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Código Postal',
                'key': 'codigo_postal',
                'placeholder': '',
                'persistent': True,
                'type': 'textfield'
            }
        ]
    },
    'contrato': {
        'title': 'Registro de Contrato',
        'name': 'registro-contrato',
        'path': 'registro-contrato',
        'components': [
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Número de Contrato',
                'key': 'numero_contrato',
                'persistent': True,
                'validate': {'required': True},
                'type': 'textfield'
            },
            {
                'input': True,
                'tableView': True,
                'type': 'select',
                'label': 'Tipo de Contrato',
                'key': 'tipo_contrato',
                'data': {
                    'values': [
                        {'label': 'Individual', 'value': 'individual'},
                        {'label': 'Familiar', 'value': 'familiar'},
                        {'label': 'Grupal', 'value': 'grupal'}
                    ]
                },
                'validate': {'required': True}
            },
            {
                'input': True,
                'tableView': True,
                'type': 'datetime',
                'label': 'Fecha de Inicio',
                'key': 'fecha_inicio',
                'validate': {'required': True}
            },
            {
                'input': True,
                'tableView': True,
                'type': 'datetime',
                'label': 'Fecha de Vencimiento',
                'key': 'fecha_vencimiento',
                'validate': {'required': True}
            },
            {
                'input': True,
                'tableView': True,
                'inputType': 'text',
                'label': 'Estado',
                'key': 'estado',
                'placeholder': 'Activo/Inactivo',
                'persistent': True,
                'type': 'textfield'
            }
        ]
    }
}


def get_form_schema(form_type):
    """
    Obtiene el esquema de formulario por tipo
    
    Args:
        form_type (str): Tipo de formulario (ej: 'cliente', 'contrato')
    
    Returns:
        dict: Esquema del formulario con propiedades adicionales
    
    Raises:
        ValueError: Si el tipo de formulario no existe
    """
    schema = schemas.get(form_type)
    if not schema:
        raise ValueError(f"Form schema for '{form_type}' not found")
    
    return {
        **schema,
        'display': 'form',
        'type': 'form',
        'tags': [form_type],
        'revisions': 'original'
    }
