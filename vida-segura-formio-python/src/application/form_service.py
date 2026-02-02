"""
FormService - Servicio de aplicación para gestionar formularios
Capa de aplicación - Lógica de negocio de formularios
"""

from src.infrastructure.http_client import http_client
from src.shared.config import FORMIO_CONFIG, HEADERS
from src.shared.logger import logger


class FormService:
    """Servicio de aplicación para gestionar formularios en Form.io"""
    
    def __init__(self):
        """Inicializa el servicio de formularios"""
        self.base_url = FORMIO_CONFIG.BASE_URL
        self.api_key = FORMIO_CONFIG.API_KEY
    
    def create_form(self, form_data):
        """
        Crear un nuevo formulario
        
        Args:
            form_data (dict): Datos del formulario a crear
        
        Returns:
            dict: Respuesta del servidor con los datos del formulario creado
        
        Raises:
            Exception: Si la creación falla
        """
        try:
            logger.info('📝 Creating form...', {
                'title': form_data.get('title'),
                'name': form_data.get('name')
            })
            
            url = f"{self.base_url}/form"
            response = http_client.post(
                url,
                form_data,
                HEADERS.WITH_API_KEY
            )
            
            logger.success('Form created successfully', {'id': response.get('_id')})
            return response
        
        except Exception as error:
            logger.error('Failed to create form', error)
            raise
    
    def update_form(self, form_id, form_data):
        """
        Actualizar un formulario existente
        
        Args:
            form_id (str): ID del formulario
            form_data (dict): Datos a actualizar
        
        Returns:
            dict: Formulario actualizado
        
        Raises:
            Exception: Si la actualización falla
        """
        try:
            logger.info('📝 Updating form...', {'id': form_id})
            
            url = f"{self.base_url}/form/{form_id}"
            response = http_client.put(
                url,
                form_data,
                HEADERS.WITH_API_KEY
            )
            
            logger.success('Form updated successfully', {'id': form_id})
            return response
        
        except Exception as error:
            logger.error('Failed to update form', error)
            raise
    
    def get_form(self, form_id):
        """
        Obtener un formulario por ID
        
        Args:
            form_id (str): ID del formulario
        
        Returns:
            dict: Datos del formulario
        
        Raises:
            Exception: Si la obtención falla
        """
        try:
            logger.info('📋 Getting form...', {'id': form_id})
            
            url = f"{self.base_url}/form/{form_id}"
            response = http_client.get(url, HEADERS.WITH_API_KEY)
            
            logger.success('Form retrieved', {'title': response.get('title')})
            return response
        
        except Exception as error:
            logger.error('Failed to get form', error)
            raise
    
    def list_forms(self):
        """
        Listar todos los formularios del proyecto
        
        Returns:
            list: Lista de formularios
        
        Raises:
            Exception: Si la listación falla
        """
        try:
            logger.info('📋 Listing forms...')
            
            url = f"{self.base_url}/form"
            response = http_client.get(url, HEADERS.WITH_API_KEY)
            
            # Si es una lista directa, retornarla
            if isinstance(response, list):
                logger.success(f'Forms retrieved', {'count': len(response)})
                return response
            
            # Si es una respuesta con estructura, obtener los forms
            forms = response.get('forms', response.get('data', []))
            logger.success(f'Forms retrieved', {'count': len(forms)})
            return forms
        
        except Exception as error:
            logger.error('Failed to list forms', error)
            raise
    
    def submit_form(self, form_id, data):
        """
        Enviar datos de un formulario
        
        Args:
            form_id (str): ID del formulario
            data (dict): Datos del formulario
        
        Returns:
            dict: Respuesta del servidor
        
        Raises:
            Exception: Si el envío falla
        """
        try:
            logger.info('📤 Submitting form...', {'id': form_id})
            
            url = f"{self.base_url}/form/{form_id}/submission"
            response = http_client.post(
                url,
                {'data': data},
                HEADERS.WITH_API_KEY
            )
            
            logger.success('Form submitted successfully', 
                          {'submissionId': response.get('_id')})
            return response
        
        except Exception as error:
            logger.error('Failed to submit form', error)
            raise


# Instancia singleton
form_service = FormService()
