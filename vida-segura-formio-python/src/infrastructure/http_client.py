"""
HttpClient - Servicio para realizar peticiones HTTP
Infraestructura - Abstracción de llamadas a la API
"""

import requests
import json
from src.shared.logger import logger


class HttpClient:
    """Cliente HTTP para comunicación con Form.io"""
    
    def __init__(self):
        """Inicializa el cliente HTTP"""
        self.session = requests.Session()
    
    def request(self, method, url, headers=None, body=None):
        """
        Realiza una petición HTTP genérica
        
        Args:
            method (str): Método HTTP (GET, POST, PUT, DELETE)
            url (str): URL del endpoint
            headers (dict): Headers de la petición
            body (dict): Cuerpo de la petición
        
        Returns:
            dict: Respuesta JSON del servidor
        
        Raises:
            Exception: Si la petición falla
        """
        try:
            if headers is None:
                headers = {}
            
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                json=body
            )
            
            if not response.ok:
                error_text = response.text[:200]
                raise Exception(
                    f"HTTP {response.status_code}: {response.reason} - {error_text}"
                )
            
            return response.json()
        
        except Exception as error:
            logger.error(f"Request failed: {method} {url}", error)
            raise
    
    def post(self, url, body, headers=None):
        """
        Realiza una petición POST
        
        Args:
            url (str): URL del endpoint
            body (dict): Cuerpo de la petición
            headers (dict): Headers opcionales
        
        Returns:
            dict: Respuesta JSON
        """
        return self.request('POST', url, headers, body)
    
    def put(self, url, body, headers=None):
        """
        Realiza una petición PUT
        
        Args:
            url (str): URL del endpoint
            body (dict): Cuerpo de la petición
            headers (dict): Headers opcionales
        
        Returns:
            dict: Respuesta JSON
        """
        return self.request('PUT', url, headers, body)
    
    def get(self, url, headers=None):
        """
        Realiza una petición GET
        
        Args:
            url (str): URL del endpoint
            headers (dict): Headers opcionales
        
        Returns:
            dict: Respuesta JSON
        """
        return self.request('GET', url, headers, None)
    
    def delete(self, url, headers=None):
        """
        Realiza una petición DELETE
        
        Args:
            url (str): URL del endpoint
            headers (dict): Headers opcionales
        
        Returns:
            dict: Respuesta JSON
        """
        return self.request('DELETE', url, headers, None)


# Instancia singleton
http_client = HttpClient()
