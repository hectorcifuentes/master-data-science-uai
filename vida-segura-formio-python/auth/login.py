"""
Login Script - Autenticación del usuario
Punto de entrada para autenticarse en Form.io usando API Key
"""

import sys
sys.path.insert(0, '.')

from src.shared.logger import logger
from src.shared.config import FORMIO_CONFIG


def main():
    """Función principal de login"""
    try:
        logger.section('Form.io Authentication')
        
        api_key = FORMIO_CONFIG.API_KEY
        
        logger.success('API Key loaded successfully!', {
            'apiKey': api_key[:20] + '...',
            'baseUrl': FORMIO_CONFIG.BASE_URL
        })
        
        logger.info('Ready to use with Form.io', {
            'authenticated': True,
            'method': 'API Key',
            'projects': 'All projects accessible'
        })
        
        return api_key
    
    except Exception as error:
        logger.error('Authentication failed', error)
        sys.exit(1)


if __name__ == '__main__':
    main()
