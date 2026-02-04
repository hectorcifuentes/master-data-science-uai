"""
Configuración de Form.io
Variables de entorno y constantes globales
"""

import os

class FORMIO_CONFIG:
    """Configuración centralizada para Form.io
    
    Antes de ejecutar el login o crear formularios, debes crear tu propio usuario y contraseña en Form.io.
    Luego, añade tu email y contraseña aquí, reemplazando los valores dummy, o usa variables de entorno.
    """
    BASE_URL = os.getenv('FORMIO_BASE_URL', 'https://dummy.form.io')
    API_KEY = os.getenv('FORMIO_API_KEY', 'DUMMY_API_KEY')
    USER_EMAIL = os.getenv('FORMIO_EMAIL', 'dummy@email.com')
    USER_PASSWORD = os.getenv('FORMIO_PASSWORD', 'dummy_password')
    PROJECT_ID = os.getenv('FORMIO_PROJECT_ID', 'dummy_project_id')


class FORM_IDS:
    """IDs de los formularios creados"""
    CLIENTE = 'dummy_cliente_id'
    CONTRATO = 'dummy_contrato_id'
    PLAN_SALUD = 'dummy_plan_salud_id'
    BENEFICIARIO = 'dummy_beneficiario_id'
    ATENCION_MEDICA = 'dummy_atencion_medica_id'
    DIAGNOSTICO = 'dummy_diagnostico_id'
    PRESTACION = 'dummy_prestacion_id'
    PRESTADOR = 'dummy_prestador_id'
    PROFESIONAL = 'dummy_profesional_id'
    COBERTURA = 'dummy_cobertura_id'
    PAGO = 'dummy_pago_id'


class HEADERS:
    """Headers predefinidos para requests"""
    JSON = {'Content-Type': 'application/json'}
    
    WITH_API_KEY = {
        'Content-Type': 'application/json',
        'x-token': FORMIO_CONFIG.API_KEY
    }
    
    @staticmethod
    def WITH_JWT(token):
        """Headers con JWT token"""
        return {
            'Content-Type': 'application/json',
            'x-jwt-token': token
        }


class ENDPOINTS:
    """Endpoints de Form.io API"""
    LOGIN = '/user/login'
    FORMS = '/form'
    SUBMISSIONS = '/submission'
    PROJECT = f'/project/{FORMIO_CONFIG.PROJECT_ID}'
