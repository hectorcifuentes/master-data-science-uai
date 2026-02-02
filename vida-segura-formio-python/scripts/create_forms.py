"""
Create Forms Script - Crear todos los formularios en Form.io
Script de inicialización
"""

import sys
sys.path.insert(0, '.')

from src.application.form_service import form_service
from src.domain.form_schemas import get_form_schema
from src.shared.logger import logger


# Lista de formularios a crear/actualizar
FORMS_TO_CREATE = [
    {'key': 'cliente', 'name': 'Cliente'},
    {'key': 'contrato', 'name': 'Contrato'},
    # Agregar más formularios aquí según sea necesario
]


def create_or_update_forms():
    """Función principal para crear/actualizar formularios"""
    try:
        logger.section('Creating Forms in Form.io')
        
        for form in FORMS_TO_CREATE:
            try:
                schema = get_form_schema(form['key'])
                logger.info(f"Processing form: {form['name']}")
                
                # Crear el formulario
                created_form = form_service.create_form(schema)
                logger.success(f"Form created: {form['name']}", {
                    'id': created_form.get('_id'),
                    'url': created_form.get('url', 'N/A')
                })
            
            except Exception as error:
                logger.warning(f"Could not create {form['name']}", str(error))
        
        logger.section('All forms processed')
    
    except Exception as error:
        logger.error('Failed to create forms', error)
        sys.exit(1)


if __name__ == '__main__':
    create_or_update_forms()
