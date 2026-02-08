/**
 * Configuración de Form.io
 * Variables de entorno y constantes globales
 */

export const FORMIO_CONFIG = {
    BASE_URL: process.env.FORMIO_BASE_URL || 'https://dummy.form.io',
    API_KEY: process.env.FORMIO_API_KEY || 'DUMMY_API_KEY',
    USER_EMAIL: process.env.FORMIO_EMAIL || 'dummy@email.com',
    USER_PASSWORD: process.env.FORMIO_PASSWORD || 'dummy_password',
    PROJECT_ID: process.env.FORMIO_PROJECT_ID || 'dummy_project_id'
};

export const FORM_IDS = {
    CLIENTE: 'dummy_cliente_id',
    CONTRATO: 'dummy_contrato_id',
    PLAN_SALUD: 'dummy_plan_salud_id',
    BENEFICIARIO: 'dummy_beneficiario_id',
    ATENCION_MEDICA: 'dummy_atencion_medica_id',
    DIAGNOSTICO: 'dummy_diagnostico_id',
    PRESTACION: 'dummy_prestacion_id',
    PRESTADOR: 'dummy_prestador_id',
    PROFESIONAL: 'dummy_profesional_id',
    COBERTURA: 'dummy_cobertura_id',
    PAGO: 'dummy_pago_id'
};

export const HEADERS = {
    JSON: { 'Content-Type': 'application/json' },
    WITH_API_KEY: {
        'Content-Type': 'application/json',
        'x-token': FORMIO_CONFIG.API_KEY
    },
    WITH_JWT: (token) => ({
        'Content-Type': 'application/json',
        'x-jwt-token': token
    })
};

export const ENDPOINTS = {
    LOGIN: '/user/login',
    USER: '/user',
    FORM: '/form',
    PROJECT: '/project'
};
