"""
Test Script - Verificar que la nueva arquitectura funciona
Prueba simple sin autenticación de usuario
"""

import sys
sys.path.insert(0, '.')

from src.application.form_service import form_service
from src.domain.form_schemas import get_form_schema
from src.shared.logger import logger


def test_forms():
    """Función principal de prueba"""
    try:
        logger.section('Testing Form Service')
        
        # Obtener el schema del formulario cliente
        cliente_schema = get_form_schema('cliente')
        
        logger.success('Schema loaded:', {
            'title': cliente_schema.get('title'),
            'name': cliente_schema.get('name'),
            'components': len(cliente_schema.get('components', []))
        })
        
        # Intentar listar formularios existentes
        logger.info('Listing existing forms...')
        forms = form_service.list_forms()
        
        logger.success('Forms retrieved:', {
            'count': len(forms) if isinstance(forms, list) else 0,
            'forms': [
                {'id': f.get('_id'), 'title': f.get('title')} 
                for f in forms[:3]
            ] if isinstance(forms, list) else []
        })
        
        logger.section('✅ All tests passed!')
    
    except Exception as error:
        logger.error('Test failed', error)
        sys.exit(1)


if __name__ == '__main__':
    test_forms()
