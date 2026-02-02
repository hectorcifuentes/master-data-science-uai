"""
AuthService - Servicio de autenticación con Form.io
Infraestructura - Lógica de autenticación
"""

from src.infrastructure.http_client import http_client
from src.shared.config import FORMIO_CONFIG, ENDPOINTS, HEADERS
from src.shared.logger import logger


class AuthService:
    """Servicio de autenticación para Form.io"""
    
    def __init__(self):
        """Inicializa el servicio de autenticación"""
        self.base_url = FORMIO_CONFIG.BASE_URL
        self.token = None
    
    def login_with_credentials(self, email, password):
        """
        Autentica usuario con email y contraseña
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
        
        Returns:
            str: Token de autenticación
        
        Raises:
            Exception: Si la autenticación falla
        """
        try:
            logger.info('🔐 Authenticating user...')
            
            url = f"{self.base_url}{ENDPOINTS.LOGIN}"
            response = http_client.post(
                url,
                {'email': email, 'password': password},
                HEADERS.JSON
            )
            
            self.token = response.get('token') or response.get('_id')
            logger.success('Authentication successful!', {
                'token': self.token[:50] + '...' if self.token else 'None'
            })
            
            return self.token
        
        except Exception as error:
            logger.error('Login failed', error)
            raise
    
    def get_token(self):
        """
        Obtiene el token actual
        
        Returns:
            str: Token de autenticación o None
        """
        return self.token
    
    def is_authenticated(self):
        """
        Verifica si hay token activo
        
        Returns:
            bool: True si está autenticado, False en caso contrario
        """
        return bool(self.token)
    
    def logout(self):
        """Limpia el token (logout)"""
        self.token = None
        logger.success('User logged out')


# Instancia singleton
auth_service = AuthService()
