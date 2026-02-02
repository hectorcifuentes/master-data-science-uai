"""
Configuración de Form.io
Variables de entorno y constantes globales
"""

import os

class FORMIO_CONFIG:
    """Configuración centralizada para Form.io"""
    BASE_URL = os.getenv('FORMIO_BASE_URL', 'https://uvcraipfxlkpugh.form.io')
    API_KEY = os.getenv('FORMIO_API_KEY', '8bIr91fH3pwQx4PvUkjCnuYAjkYwPL')
    USER_EMAIL = os.getenv('FORMIO_EMAIL', 'cifuentesmella.hector@gmail.com')
    USER_PASSWORD = os.getenv('FORMIO_PASSWORD', 'Tito6223')
    PROJECT_ID = os.getenv('FORMIO_PROJECT_ID', '697e681fff4c95368619b1f6')


class FORM_IDS:
    """IDs de los formularios creados"""
    CLIENTE = '697ebba1cd4b046138f5e4ee'
    CONTRATO = '697ebf91db796af904668b44'
    PLAN_SALUD = '697ec2d5cd4b046138f602bd'
    BENEFICIARIO = '697ec50acd4b046138f61017'
    ATENCION_MEDICA = '697ec966db796af90466bbcc'
    DIAGNOSTICO = '697eca2acd4b046138f627d6'
    PRESTACION = '697eca2acd4b046138f627df'
    PRESTADOR = '697eca2adb796af90466c05f'
    PROFESIONAL = '697eca2acd4b046138f627ea'
    COBERTURA = '697eca2adb796af90466c05c'
    PAGO = '697eca2acd4b046138f627e7'


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
