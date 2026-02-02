/**
 * Configuración de Form.io
 * Variables de entorno y constantes globales
 */

export const FORMIO_CONFIG = {
    BASE_URL: process.env.FORMIO_BASE_URL || 'https://uvcraipfxlkpugh.form.io',
    API_KEY: process.env.FORMIO_API_KEY || '8bIr91fH3pwQx4PvUkjCnuYAjkYwPL',
    USER_EMAIL: process.env.FORMIO_EMAIL || 'cifuentesmella.hector@gmail.com',
    USER_PASSWORD: process.env.FORMIO_PASSWORD || 'Tito6223',
    PROJECT_ID: process.env.FORMIO_PROJECT_ID || '697e681fff4c95368619b1f6'
};

export const FORM_IDS = {
    CLIENTE: '697ebba1cd4b046138f5e4ee',
    CONTRATO: '697ebf91db796af904668b44',
    PLAN_SALUD: '697ec2d5cd4b046138f602bd',
    BENEFICIARIO: '697ec50acd4b046138f61017',
    ATENCION_MEDICA: '697ec966db796af90466bbcc',
    DIAGNOSTICO: '697eca2acd4b046138f627d6',
    PRESTACION: '697eca2acd4b046138f627df',
    PRESTADOR: '697eca2adb796af90466c05f',
    PROFESIONAL: '697eca2acd4b046138f627ea',
    COBERTURA: '697eca2adb796af90466c05c',
    PAGO: '697eca2acd4b046138f627e7'
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
