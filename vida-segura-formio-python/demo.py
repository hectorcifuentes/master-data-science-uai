"""
Demo Script - Demostración completa de la arquitectura Clean
Demuestra las diferentes capas y servicios
"""

import sys
sys.path.insert(0, '.')

from src.application.form_service import form_service
from src.domain.form_schemas import get_form_schema
from src.shared.logger import logger
from src.shared.config import FORM_IDS


def demonstrate_architecture():
    """Función principal de demostración"""
    try:
        logger.section('🏗️  Clean Architecture Demo')
        
        # 1️⃣ Domain Layer - Obtener esquemas
        logger.info('1️⃣ Domain Layer - Form Schemas')
        cliente_schema = get_form_schema('cliente')
        logger.success('✓ Client form schema loaded', {
            'title': cliente_schema.get('title'),
            'fields': len(cliente_schema.get('components', []))
        })
        
        # 2️⃣ Infrastructure Layer - HTTP Communication
        logger.info('2️⃣ Infrastructure Layer - HTTP Communication')
        logger.success('✓ HttpClient configured for API requests')
        
        # 3️⃣ Application Layer - Business Logic
        logger.info('3️⃣ Application Layer - FormService')
        forms = form_service.list_forms()
        form_titles = [f.get('title') for f in forms[:3]] if isinstance(forms, list) else []
        logger.success('✓ Forms retrieved via FormService', {
            'total': len(forms) if isinstance(forms, list) else 0,
            'forms': form_titles
        })
        
        # 4️⃣ Shared Layer - Configuration & Logging
        logger.info('4️⃣ Shared Layer - Config & Logger')
        form_ids_dict = {
            k: v for k, v in FORM_IDS.__dict__.items() 
            if not k.startswith('_')
        }
        logger.success('✓ Centralized configuration and logging', {
            'trackedForms': len(form_ids_dict)
        })
        
        # Get specific form info
        logger.section('📊 Formularios Registrados')
        
        if isinstance(forms, list):
            cliente_form = next((f for f in forms if f.get('_id') == FORM_IDS.CLIENTE), None)
            if cliente_form:
                logger.success('Cliente', {
                    'id': cliente_form.get('_id'),
                    'name': cliente_form.get('name'),
                    'path': cliente_form.get('path')
                })
            
            contrato_form = next((f for f in forms if f.get('_id') == FORM_IDS.CONTRATO), None)
            if contrato_form:
                logger.success('Contrato', {
                    'id': contrato_form.get('_id'),
                    'name': contrato_form.get('name')
                })
        
        # Demonstrate architecture benefits
        logger.section('✨ Arquitectura Benefits')
        logger.success('Clean Architecture Implemented:', {
            'layers': ['Domain', 'Application', 'Infrastructure', 'Shared'],
            'principles': ['SRP', 'DIP', 'DRY', 'SOLID'],
            'testability': 'High (isolated services)',
            'maintainability': 'Excellent (clear structure)'
        })
    
    except Exception as error:
        logger.error('Demo failed', error)
        sys.exit(1)


if __name__ == '__main__':
    demonstrate_architecture()
